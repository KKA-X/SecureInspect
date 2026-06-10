from src.analyzer import (
    analyze_changes,
    calculate_risk
)

def test_new_file_detection():

    baseline = {
        "a.txt": "111"
    }

    current = {
        "a.txt": "111",
        "b.txt": "222"
    }

    report = analyze_changes(
        baseline,
        current
    )

    assert report["new_files"] == ["b.txt"]
    assert report["deleted_files"] == []
    assert report["modified_files"] == []

def test_deleted_file_detection():

    baseline = {
        "a.txt": "111",
        "b.txt": "222"
    }

    current = {
        "a.txt": "111"
    }

    report = analyze_changes(
        baseline,
        current
    )

    assert report["new_files"] == []
    assert report["deleted_files"] == ["b.txt"]
    assert report["modified_files"] == []

def test_modified_file_detection():

    baseline = {
        "a.txt": "111"
    }

    current = {
        "a.txt": "999"
    }

    report = analyze_changes(
        baseline,
        current
    )

    assert report["new_files"] == []
    assert report["deleted_files"] == []
    assert report["modified_files"] == ["a.txt"]

def test_safe_risk():

    report = {
        "new_files": [],
        "deleted_files": [],
        "modified_files": []
    }

    score, status = calculate_risk(report)

    assert score == 0
    assert status == "SAFE"

def test_attention_required_risk():

    report = {
        "new_files": ["a.txt"],
        "deleted_files": [],
        "modified_files": []
    }

    score, status = calculate_risk(report)

    assert score == 10
    assert status == "ATTENTION REQUIRED"

def test_high_risk():

    report = {
        "new_files": ["a.txt", "b.txt"],
        "deleted_files": ["c.txt", "d.txt"],
        "modified_files": ["e.txt", "f.txt"]
    }

    score, status = calculate_risk(report)

    assert score > 50
    assert status == "HIGH RISK"

def test_score_capped_at_100():

    report = {
        "new_files": ["a"] * 20,
        "deleted_files": ["b"] * 20,
        "modified_files": ["c"] * 20
    }

    score, _ = calculate_risk(report)

    assert score == 100