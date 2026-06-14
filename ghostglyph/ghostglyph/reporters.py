from pathlib import Path
from colorama import Fore, init
import csv
import json

init(autoreset=True)

def print_banner():

    print(
        Fore.CYAN
        + """
========================================
      GhostGlyph Security Scanner
   Invisible Unicode Threat Detector
========================================
"""
    )

def print_report(file_name, findings):

    print_banner()

    print(Fore.WHITE + f"File Scanned : {file_name}")
    print(Fore.WHITE + f"Threats Found: {len(findings)}\n")

    if not findings:
        print(Fore.GREEN + "[OK] No threats detected.")
        return

    for item in findings:

        print(Fore.YELLOW + "-" * 40)

        if item.get("type") == "unicode":

            color = (
                Fore.RED
                if item.get("risk") == "CRITICAL"
                else Fore.MAGENTA
            )

            print(
                color
                + f"[{item.get('risk')}] Unicode Threat Detected"
            )

            print(
                Fore.WHITE
                + f"Location : {item.get('position')}"
            )

            print(
                Fore.WHITE
                + f"Codepoint: {item.get('unicode')}"
            )

            print(
                Fore.WHITE
                + f"Name     : {item.get('name')}"
            )

        elif item.get("type") == "homoglyph":

            print(
                Fore.RED
                + "[HIGH] Homoglyph Attack Detected"
            )

            print(
                Fore.WHITE
                + f"Position : {item.get('position')}"
            )

            print(
                Fore.WHITE
                + f"Character: {item.get('character')}"
            )

            print(
                Fore.WHITE
                + f"Looks Like: {item.get('looks_like')}"
            )

    print(Fore.YELLOW + "\n========================================")

    print(Fore.CYAN + "[SUMMARY]")
    print(Fore.WHITE + f"Total Threats: {len(findings)}")

def export_json(file, findings):

    path = Path(file).expanduser()

    with path.open(
        "w",
        encoding="utf-8"
    ) as f:

        if findings:

            json.dump(
                findings,
                f,
                indent=4,
                ensure_ascii=False
            )

        else:

            json.dump(
                {
                    "message": "No threats detected"
                },
                f,
                indent=4
            )

    return str(path.resolve())

def export_csv(file, findings):

    path = Path(file).expanduser()

    with path.open(
        "w",
        newline="",
        encoding="utf-8"
    ) as f:

        if findings:

            writer = csv.DictWriter(
                f,
                fieldnames=findings[0].keys()
            )

            writer.writeheader()
            writer.writerows(findings)

        else:

            writer = csv.writer(f)

            writer.writerow([
                "message"
            ])

            writer.writerow([
                "No threats detected"
            ])

    return str(path.resolve())