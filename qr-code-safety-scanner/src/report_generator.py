import json

def save_reports(report):
    with open("report.json","w") as f:
        json.dump(report, f, indent=2)

    with open("report.txt","w") as f:
        f.write("QR CODE SAFETY REPORT\n")
        f.write("=" * 30 + "\n")
        for k,v in report.items():
            f.write(f"{k}: {v}\n")
