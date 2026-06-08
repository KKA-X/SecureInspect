import json
import tempfile
from pathlib import Path

from src.analyzer import analyze
from src.report_generator import save_reports


def test_report_json_creation():
    data = analyze("https://example.com")

    with tempfile.TemporaryDirectory() as temp_dir:
        old_cwd = Path.cwd()

        try:
            import os
            os.chdir(temp_dir)

            save_reports(data)

            assert Path("report.json").exists()

            with open("report.json", "r") as f:
                report = json.load(f)

            assert report["content"] == "https://example.com"
            assert report["risk_score"] == 0
            assert report["risk_level"] == "SAFE"

        finally:
            os.chdir(old_cwd)


def test_report_txt_creation():
    data = analyze("https://example.com")

    with tempfile.TemporaryDirectory() as temp_dir:
        old_cwd = Path.cwd()

        try:
            import os
            os.chdir(temp_dir)

            save_reports(data)

            assert Path("report.txt").exists()

            text = Path("report.txt").read_text()

            assert "https://example.com" in text
            assert "SAFE" in text

        finally:
            os.chdir(old_cwd)


def test_report_files_created_together():
    data = analyze("http://fake.xyz/login")

    with tempfile.TemporaryDirectory() as temp_dir:
        old_cwd = Path.cwd()

        try:
            import os
            os.chdir(temp_dir)

            save_reports(data)

            assert Path("report.json").exists()
            assert Path("report.txt").exists()

        finally:
            os.chdir(old_cwd)