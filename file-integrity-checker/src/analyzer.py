def analyze_changes(baseline, current):

    report = {
        "new_files": [],
        "deleted_files": [],
        "modified_files": []
    }

    baseline_files = set(baseline.keys())
    current_files = set(current.keys())

    report["new_files"] = sorted(
        current_files - baseline_files
    )

    report["deleted_files"] = sorted(
        baseline_files - current_files
    )

    for file in baseline_files.intersection(current_files):

        if baseline[file] != current[file]:

            report["modified_files"].append(file)

    report["modified_files"].sort()

    return report

def calculate_risk(report):

    score = 0

    score += len(report["new_files"]) * 10
    score += len(report["deleted_files"]) * 20
    score += len(report["modified_files"]) * 25

    score = min(score, 100)

    if score == 0:

        status = "SAFE"

    elif score <= 50:

        status = "ATTENTION REQUIRED"

    else:

        status = "HIGH RISK"

    return score, status