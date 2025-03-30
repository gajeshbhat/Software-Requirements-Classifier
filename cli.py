import argparse
import os
from app.classify import classify_requirements_via_api
from app.document_parser import parse_input
from app.exporter import export_console, export_pdf, export_json

def main():
    parser = argparse.ArgumentParser(description="Software Requirements Classifier using LLM")
    parser.add_argument("--input", help="Path to input file OR requirement string", required=False)
    parser.add_argument("--output-json", help="Path to save JSON results", required=False)
    parser.add_argument("--output-pdf", help="Path to save PDF report", required=False)
    parser.add_argument("--console", action="store_true", help="Print results to console")
    parser.add_argument("--model", help="Ollama model name", default="codellama:instruct")
    
    args = parser.parse_args()

    # 1. Parse input
    requirements = parse_input(args.input)

    # 2. Classify via Ollama
    results = classify_requirements_via_api(requirements, model=args.model)

    # 3. Export results
    if args.output_json:
        export_json(results, args.output_json)
    if args.output_pdf:
        export_pdf(results, args.output_pdf)
    if args.console or not (args.output_json or args.output_pdf):
        export_console(results)

if __name__ == "__main__":
    main()
