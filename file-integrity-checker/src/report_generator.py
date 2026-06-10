import json

def save_reports(report, score, status):

    output = {
        "report": report,
        "risk_score": score,
        "status": status
    }

    with open(
        "integrity_report.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            output,
            file,
            indent=4
        )

    with open(
        "integrity_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("FILE INTEGRITY REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Risk Score: {score}\n")
        file.write(f"Status: {status}\n\n")

        file.write("NEW FILES\n")
        file.write("-" * 20 + "\n")

        if report["new_files"]:

            for item in report["new_files"]:
                file.write(f"{item}\n")

        else:

            file.write("None\n")

        file.write("\n")

        file.write("DELETED FILES\n")
        file.write("-" * 20 + "\n")

        if report["deleted_files"]:

            for item in report["deleted_files"]:
                file.write(f"{item}\n")

        else:

            file.write("None\n")

        file.write("\n")

        file.write("MODIFIED FILES\n")
        file.write("-" * 20 + "\n")

        if report["modified_files"]:

            for item in report["modified_files"]:
                file.write(f"{item}\n")

        else:

            file.write("None\n")