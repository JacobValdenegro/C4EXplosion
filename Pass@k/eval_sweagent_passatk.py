import os
import subprocess
import json
import csv
import re
from pathlib import Path

REPO_URL = "https://github.com/JacobV321/swe-agent-test"
CONFIG_PATH = "/config/coding_challenge.yaml"
PROBLEMS_FILE = "problems.txt"
OUTPUT_DIR = "./evaluations"
RUN_ATTEMPTS = 3
CSV_LOG = "metrics.csv"
JSONL_TESTS = "./test.jsonl"

def ejecutar_sweagent(url_problema, intento, issue_tag):
    resultado_dir = os.path.join(OUTPUT_DIR, f"{issue_tag}_run{intento}")
    os.makedirs(resultado_dir, exist_ok=True)

    comando = [
        "sweagent", "run",
        "--config", CONFIG_PATH,
        f"--env.repo.github_url={REPO_URL}",
        f"--problem_statement.github_url={url_problema}"
    ]

    print(f"🏃 Ejecutando intento {intento+1} para {issue_tag}...")
    resultado = subprocess.run(comando, capture_output=True, text=True)

    with open(os.path.join(resultado_dir, "stdout.txt"), "w") as f:
        f.write(resultado.stdout)
    with open(os.path.join(resultado_dir, "stderr.txt"), "w") as f:
        f.write(resultado.stderr)

    return resultado_dir

def extraer_patch(stdout_log):
    match = re.search(r"PATCH_FILE_PATH='([^']+)'", stdout_log)
    if match:
        return match.group(1).strip()
    return None

def aplicar_patch(patch_path, repo_path):
    try:
        subprocess.run(["git", "apply", patch_path], cwd=repo_path, check=True, capture_output=True, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error aplicando patch: {e.stderr}")
        return False

def evaluar_resultado(run_dir):
    log_path = os.path.join(run_dir, "stdout.txt")
    if not os.path.exists(log_path):
        return False

    with open(log_path, "r") as f:
        contenido = f.read()

    if "🎉 Submission successful 🎉" in contenido:
        patch_path = extraer_patch(contenido)
        if patch_path and os.path.isfile(patch_path):
            repo_eval = "/Users/estebanm/Documents/C3Agent/C3Agent/pass@k/runs/Test_C3"
            return aplicar_patch(patch_path, repo_eval)
    return False

def passk_metrica(resultados):
    for idx, exito in enumerate(resultados, 1):
        if exito:
            return 1.0 / idx
    return 0.0

def main():
    with open(PROBLEMS_FILE, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    resumen = []

    for url in urls:
        issue = url.split("/")[-1]
        intentos = []
        print(f"🔍 Evaluando issue {issue}")

        for i in range(RUN_ATTEMPTS):
            carpeta = ejecutar_sweagent(url, i, issue)
            correcto = evaluar_resultado(carpeta)
            intentos.append(correcto)
            if correcto:
                break

        metrica = passk_metrica(intentos)
        resumen.append({
            "issue": issue,
            "exitos": int(any(intentos)),
            "intentos": len(intentos),
            "pass@k": round(metrica, 3)
        })

    with open(CSV_LOG, "w", newline="") as csvfile:
        campos = ["issue", "exitos", "intentos", "pass@k"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)
        writer.writeheader()
        for fila in resumen:
            writer.writerow(fila)

    promedio = sum(x["pass@k"] for x in resumen) / len(resumen)
    print(f"Evaluaciones completadas: {len(resumen)}")
    print(f"Promedio pass@k: {promedio:.3f}")
    print(f"Resultados exportados en: {CSV_LOG}")

if __name__ == "__main__":
    main()
