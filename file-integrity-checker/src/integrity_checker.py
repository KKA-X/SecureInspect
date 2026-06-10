import os
import sys

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

from hashing import calculate_sha256
from baseline_manager import (
    save_baseline,
    load_baseline
)

from analyzer import (
    analyze_changes,
    calculate_risk
)

from report_generator import save_reports

console = Console()

def scan_directory(directory):

    hashes = {}

    for root, _, files in os.walk(directory):

        for file in files:

            path = os.path.join(root, file)

            try:

                hashes[path] = calculate_sha256(path)

            except Exception as e:

                console.print(
                    f"[yellow]Warning:[/yellow] Could not process {path}: {e}"
                )

    return hashes

def create_baseline(directory):

    if not os.path.isdir(directory):

        console.print(
            "[bold red]Directory not found.[/bold red]"
        )

        return

    hashes = scan_directory(directory)

    save_baseline(hashes)

    console.print(
        "[bold green]✓ Baseline Created Successfully[/bold green]"
    )

def verify_integrity(directory):

    if not os.path.isdir(directory):

        console.print(
            "[bold red]Directory not found.[/bold red]"
        )

        return

    baseline = load_baseline()

    current = scan_directory(directory)

    report = analyze_changes(
        baseline,
        current
    )

    score, status = calculate_risk(report)

    console.print(
        Panel.fit(
            "[bold cyan]SecureInspect[/bold cyan]\n[white]File Integrity Checker[/white]",
            border_style="cyan"
        )
    )

    table = Table(
        title="Integrity Analysis",
        box=box.DOUBLE_EDGE
    )

    table.add_column("Metric")
    table.add_column("Value")

    table.add_row(
        "New Files",
        str(len(report["new_files"]))
    )

    table.add_row(
        "Deleted Files",
        str(len(report["deleted_files"]))
    )

    table.add_row(
        "Modified Files",
        str(len(report["modified_files"]))
    )

    table.add_row(
        "Risk Score",
        str(score)
    )

    if status == "SAFE":

        status_display = "[bold green]SAFE[/bold green]"

    elif status == "ATTENTION REQUIRED":

        status_display = "[bold yellow]ATTENTION REQUIRED[/bold yellow]"

    else:

        status_display = "[bold red]HIGH RISK[/bold red]"

    table.add_row(
        "Status",
        status_display
    )

    console.print(table)

    if report["new_files"]:

        console.print(
            "\n[bold yellow]New Files[/bold yellow]"
        )

        for file in report["new_files"]:
            console.print(f"• {file}")

    if report["deleted_files"]:

        console.print(
            "\n[bold red]Deleted Files[/bold red]"
        )

        for file in report["deleted_files"]:
            console.print(f"• {file}")

    if report["modified_files"]:

        console.print(
            "\n[bold red]Modified Files[/bold red]"
        )

        for file in report["modified_files"]:
            console.print(f"• {file}")

    save_reports(
        report,
        score,
        status
    )

    console.print(
        "\n[bold green]Reports Generated[/bold green]"
    )

def main():

    if len(sys.argv) != 3:

        console.print(
            "[bold yellow]Usage:[/bold yellow]"
        )

        console.print(
            "python integrity_checker.py --create <folder>"
        )

        console.print(
            "python integrity_checker.py --verify <folder>"
        )

        return

    command = sys.argv[1]
    directory = sys.argv[2]

    if command == "--create":

        create_baseline(directory)

    elif command == "--verify":

        verify_integrity(directory)

    else:

        console.print(
            "[bold red]Invalid command[/bold red]"
        )

if __name__ == "__main__":
    main()