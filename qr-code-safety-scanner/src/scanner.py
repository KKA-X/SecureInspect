import sys
import cv2
from pyzbar.pyzbar import decode
from src.analyzer import analyze
from src.report_generator import save_reports

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()


from pathlib import Path

def read_qr(image_path):

    path = Path(image_path)

    if not path.exists():
        raise FileNotFoundError(image_path)

    image = cv2.imread(str(path))

    if image is None:
        raise ValueError("Invalid image file")

    decoded = decode(image)

    if not decoded:
        raise ValueError("No QR code found")

    return decoded[0].data.decode("utf-8")


def display_report(report):

    console.print(
        Panel.fit(
            "[bold cyan]SecureInspect[/bold cyan]\n[white]QR Code Safety Scanner[/white]",
            border_style="cyan"
        )
    )

    console.print("[bold blue][+] Reading QR Image...[/bold blue]")
    console.print("[bold blue][+] Decoding QR Code...[/bold blue]")
    console.print("[bold blue][+] Running Security Analysis...[/bold blue]\n")

    table = Table(
        title="Scan Results",
        box=box.DOUBLE_EDGE
    )

    table.add_column("Field", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")

    table.add_row("Content", report["content"])
    table.add_row("Risk Score", str(report["risk_score"]))

    if report["risk_level"] == "SAFE":
        risk_level = "[bold green]SAFE[/bold green]"

    elif report["risk_level"] == "MEDIUM":
        risk_level = "[bold yellow]MEDIUM[/bold yellow]"

    else:
        risk_level = "[bold red]HIGH RISK[/bold red]"

    table.add_row("Risk Level", risk_level)

    console.print(table)

    if report["warnings"]:

        console.print("\n[bold red]Detected Indicators[/bold red]")

        for warning in report["warnings"]:
            console.print(
                f"⚠ {warning}",
                style="yellow"
            )

    else:

        console.print(
            "\n✓ No suspicious indicators detected.",
            style="bold green"
        )

    console.print(
        "\n[bold green]Reports Generated Successfully[/bold green]"
    )

    console.print("📄 report.json")
    console.print("📄 report.txt")


def main():

    if len(sys.argv) != 2:

        console.print(
            "Usage: python scanner.py <image>",
            style="bold red"
        )

        return

    try:

        content = read_qr(sys.argv[1])

        if not content:

            console.print(
                "No QR code found.",
                style="bold yellow"
            )

            return

        report = analyze(content)

        display_report(report)

        save_reports(report)

    except FileNotFoundError:

        console.print(
            "Image file not found.",
            style="bold red"
        )

    except Exception as e:

        console.print(
            f"Error: {e}",
            style="bold red"
        )


if __name__ == "__main__":
    main()