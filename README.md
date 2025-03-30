# Software Requirements Classifier (LLM-powered via Ollama)

This is a command-line tool to **analyze and classify software requirements** using a local LLM served via [Ollama](https://ollama.com/). It supports both structured files and free-text input, and classifies requirements into categories like:

- Functional
- Non-Functional
- Performance
- Design
- Maintenance
- Ambiguous, Incomplete, etc.

Ideal for embedded systems, product specs, and agile teams that want **AI-powered requirements triage** 🔍⚡

## 🚀 Features

- 📂 Input via `.txt`, `.pdf`, or raw string
- 📤 Output to:
  - Console
  - PDF
  - JSON
- 🧠 Powered by **local LLMs** via `ollama`
- 💡 Built-in support for models like `codellama:instruct`
- 🐳 Docker-ready: prebuilt image with model loaded
- 🧪 Extensible and testable Python code


## 📦 Local Setup (Python CLI)

For developers who want to run the CLI directly

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/software-requirements-classifier.git
cd software-requirements-classifier
```

### 2. Set up Python environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install .
```

### 3. Run the CLI

```bash
reqclass --input "The system must respond in under 2 seconds." --console
```

```bash
reqclass --input path/to/reqs.txt --output report.pdf --output-json results.json
```


## 🐳 Docker Setup (LLM Backend)

This project uses a custom `ollama` Docker image with the LLM model **preloaded**.

### 1. Build Docker Image (If you want to customize)

```bash
docker compose build
```

**Note:** This step is optional. Please make sure you change `gajesh` to your Docker Hub username in the `docker-compose.yml` file if you want to push the image.

Or pull from Docker Hub (if you did not build the image locally):
```bash
docker pull gajesh/ollama-requirements-classifier
```

### 2. Run LLM server

```bash
docker compose up -d
```

This exposes the LLM at `http://localhost:11434`

## 📘 Usage Examples

### From file:
```bash
reqclass --input tests/test_0_thermostat.txt --output report.pdf --output-json results.json
```

### From raw text:
```bash
reqclass --input "The thermostat should log humidity every 10 minutes." --console
```

## ⚠️ Limitations

- 🧠 This tool relies on **open-source LLMs** like `codellama:instruct`
- LLM output may sometimes be:
  - Vague
  - Over-generalized
  - Sensitive to phrasing
- Strict formatting is enforced, but **not 100% guaranteed** (due to model limitations)
- Does not currently support batch processing of multiple documents

## 👤 Author

Made with ❤️ by [Gajesh Bhat](https://github.com/gajeshbhat)

## 🪪 License

MIT License — free to use, fork, and build on.