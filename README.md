# 💥 C4 Explosion Agent

C4 Explosion is a powerful AI assistant designed to interpret, analyze, and automate tasks related to **customs regulations, tariff classification**, and **international trade documentation**. It is built on a fine-tuned language model using the `detonators_model_aranceles` and provides fast, structured, and accurate responses for trade professionals, customs brokers, and compliance teams.

---

## 🚀 Features

- 🧠 Deep understanding of **tariff codes, aranceles, and fracciones arancelarias**.
- 📚 Reads and interprets official documents (e.g. LIGIE, NOMs, pedimentos).
- 📊 Calculates applicable duties and taxes (IVA, IEPS, DTA) from uploaded data.
- 📝 Generates structured responses, tables, and formulas based on regulatory criteria.
- 🔎 Extracts, validates and interprets fields from customs declarations and invoices.

---

## 📦 File Structure

```
.
├── config/
│   └── c4_explosion.yaml   # Agent configuration
├── README.md               # This file
```

---

## ⚙️ Configuration Overview

The agent uses the following settings in its YAML configuration:

- **Model**: `ollama/ben1000496/detonators_model_aranceles`
- **API Base**: `http://localhost:11434`
- **Parser Function**: `thought_action` mode for reasoning and structured execution.
- **Tools**: Bash tool enabled for script execution or local validation tasks.

System prompt includes:
> "You are a multilingual AI assistant specialized in analyzing and interpreting legal, fiscal, and trade documents, with deep expertise in tariffs, customs codes, and international trade regulations..."

---

## 🧪 Usage Scenarios

- **Tariff classification**: Given a product description, suggest the correct fracción arancelaria.
- **Duty estimation**: Calculate applicable taxes for a given CIF value, HS code, and import regime.
- **Document review**: Upload pedimentos or invoices and validate content.
- **NOM/NMX/NAD compliance checks**.

---

## 🛠️ Getting Started

1. Clone the repository or install in your agent's directory.
2. Start your Ollama-compatible backend:
   ```bash
   ollama serve
   ```
3. Launch the agent:
   ```bash
   sweagent run --config config/c4_explosion.yaml
   ```

---

## 🧩 Requirements

- Python 3.10+
- [`ollama`](https://ollama.ai) installed and running locally
- `sweagent` framework (v1.1+)

---

## 📢 Notes

- This agent is **not intended to replace legal or customs advice**. It should be used as a support tool for analysis, not as the sole decision-maker.
- For best results, input complete and detailed descriptions or documents.

---

## 🧑‍💼 Authors

**Benjamín Gutiérrez Mendoza**
**Jacob Valdenegro Monzón**  
**Josue Daniel Bahena Panécatl**
**Paola Félix Torres**
**Roberto Angel Rillo Calva**
Tecnológico de Monterrey · TC3002B · *Enhancing Coder Agents for Issue Fixing with Compiler Techniques*

---

## 📜 License

This project is for academic and research use. Contact the authors for commercial licensing.
