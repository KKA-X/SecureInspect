from ghostglyph.scanner import (
    scan_text,
    calculate_risk_score
)

def test_zero_width_space_detection():

    text = "ad\u200Bmin"

    findings = scan_text(text)

    assert len(findings) == 1
    assert findings[0]["unicode"] == "U+200B"

def test_clean_text():

    text = "administrator"

    findings = scan_text(text)

    assert len(findings) == 0

def test_rtl_override_detection():

    text = "abc\u202E123"

    findings = scan_text(text)

    assert len(findings) == 1
    assert findings[0]["risk"] == "CRITICAL"

def test_risk_score():

    findings = [
        {
            "risk": "HIGH",
            "type": "unicode"
        }
    ]

    score = calculate_risk_score(findings)

    assert score == 20

def test_empty_text():

    findings = scan_text("")

    assert findings == []

def test_mixed_threats():

    text = "gοοgle\u200B"

    findings = scan_text(text)

    assert len(findings) == 3