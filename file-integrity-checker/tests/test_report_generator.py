import json

from src.report_generator import save_reports

def test_json_report_created(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    report = {
        "new_files": [],
        "deleted_files": [],
        "modified_files": []
    }

    save_reports(
        report,
        0,
        "SAFE"
    )

    assert (tmp_path / "integrity_report.json").exists()

def test_txt_report_created(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    report = {
        "new_files": [],
        "deleted_files": [],
        "modified_files": []
    }

    save_reports(
        report,
        0,
        "SAFE"
    )

    assert (tmp_path / "integrity_report.txt").exists()

def test_json_report_content(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    report = {
        "new_files": ["file1.txt"],
        "deleted_files": [],
        "modified_files": []
    }

    save_reports(
        report,
        10,
        "ATTENTION REQUIRED"
    )

    with open(
        "integrity_report.json",
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    assert data["risk_score"] == 10
    assert data["status"] == "ATTENTION REQUIRED"

def test_txt_report_content(tmp_path, monkeypatch):

    monkeypatch.chdir(tmp_path)

    report = {
        "new_files": ["file1.txt"],
        "deleted_files": [],
        "modified_files": []
    }

    save_reports(
        report,
        10,
        "ATTENTION REQUIRED"
    )

    text = (
        tmp_path /
        "integrity_report.txt"
    ).read_text()

    assert "Risk Score" in text
    assert "ATTENTION REQUIRED" in text