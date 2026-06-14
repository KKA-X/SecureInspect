import argparse
from pathlib import Path

from .scanner import scan_file
from .reporters import (
    print_report,
    export_json,
    export_csv
)

def main():

    parser = argparse.ArgumentParser(
        prog="ghostglyph",
        description="Invisible Unicode Threat Detector"
    )

    parser.add_argument(
        "target",
        help="File to scan"
    )

    parser.add_argument(
        "--json",
        help="Export findings as JSON"
    )

    parser.add_argument(
        "--csv",
        help="Export findings as CSV"
    )

    args = parser.parse_args()

    target = Path(
        args.target
    ).expanduser()

    if not target.exists():

        parser.error(
            f"File not found: {target}"
        )

    findings = scan_file(target)

    print_report(
        target.name,
        findings
    )

    if args.json:

        json_path = export_json(
            args.json,
            findings
        )

        print(
            f"[OK] JSON exported → {json_path}"
        )

    if args.csv:

        csv_path = export_csv(
            args.csv,
            findings
        )

        print(
            f"[OK] CSV exported → {csv_path}"
        )

if __name__ == "__main__":
    main()