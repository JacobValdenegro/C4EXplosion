# 💥 OOP AI-Agent for Automated Bug Fixing

C4EXplosion is an AI agent that extends SWE-Agent to automatically locate and fix bugs in Object-Oriented Programming (OOP) code.
It integrates compiler-inspired analysis and a fine-tuned Qwen2.5 model, achieving more accurate and reliable patches than baseline agents.

## 🚀 Features

*   **Structured Code Analysis:** We developed a custom compiler to classify OOP-style code and filter training data, ensuring semantic consistency.
*   **Fine-Tuned Language Model (LLM):** A curated dataset of OOP Python examples was used to fine-tune a Qwen2.5 14B-Instruct model using QLoRA on Modal's A100 GPUs.
*   **Improved Performance:** The fine-tuned model outperformed SWE-Fixer and base SWE-Agent baselines, achieving significant improvements in functional correctness and patch quality.
*   **Hybrid Approach:** Integrates classic compiler design with modern LLM-based AI techniques to enhance the accuracy and reliability of automated bug fixing.
*   **Modular Architecture:** Designed to allow future improvements with additional code features, new classifiers, or specialized datasets.


## 📦 File Structure

```
.
├── SWE-agent/
│   └── config/ # Agent configuration
├── Pass@k/     # Evaluation and metrics
```

---

## ⚙️ Configuration Overview

The agent uses the following settings in its YAML configuration:

- **Model**: `ollama/ben100496/qwen2.5-14b-guff`
- **API Base**: `http://localhost:11434`
- **Parser Function**: `thought_action` mode for reasoning and structured execution.
- **Tools**: Bash tool enabled for script execution or local validation tasks.

---

## 📊 Key Results

| Method                           | Correct Patch (%) | Partial Fix (%) | Invalid Patch (%) |
| :------------------------------- | :------------------ | :----------------- | :------------------ |
| SWE-fixer Xie et al. [2025]      | 76.3                | 12.5               | 11.2                |
| Our Method (Fine-Tuned Qwen2.5) | **86.7**            | 8.0                | **5.3**             |
---

## 🛠️ Getting Started

1. Clone the repository or install in your agent's directory.
2. Start your Ollama-compatible backend:
   ```bash
   ollama serve
   ```
3. Launch the agent:
   ```bash
   sweagent run --config config/final_config.yaml
   ```

---

## 🧩 Requirements

- Python 3.10+
- [`ollama`](https://ollama.ai) installed and running locally
- `sweagent` framework (v1.1+)

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
