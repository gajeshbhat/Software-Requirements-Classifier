import argparse
import os
from app.classify import classify_text
from app.document_parser import parse_document
from app.export import export_to_pdf, export_to_json, print_to_console

def main():
    parser = argparse.ArgumentParser(description="Software Requirements Classifier")
    parser.add_argument("--input", type=str, required=True,
                        help="Input .txt/.pdf file path OR raw requirement string")
    parser.add_argument("--output", type=str, help="Output PDF file path")
    parser.add_argument("--output-json", type=str, help="Output JSON file path")
    parser.add_argument("--console", action="store_true", help="Print results to console")
    args = parser.parse_args()

    # Read input
    if os.path.isfile(args.input):
        text = parse_document(args.input)
    else:
        text = args.input  # Treat as raw string

    # Classify
    results = classify_text(text)

    # Outputs
    if args.console or not (args.output or args.output_json):
        print_to_console(results)

    if args.output:
        export_to_pdf(results, args.output)

    if args.output_json:
        export_to_json(results, args.output_json)

if __name__ == "__main__":
    main()
