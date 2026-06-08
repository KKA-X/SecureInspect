from src.risk_engine import calculate_score


def test_safe_score():
    score, level = calculate_score([])
    assert score == 0
    assert level == "SAFE"


def test_non_https_score():
    score, level = calculate_score(["non_https"])
    assert score > 0


def test_score_capped():
    flags = [
        "non_https",
        "shortener",
        "ip_url",
        "suspicious_tld",
        "suspicious_keyword",
        "suspicious_keyword",
        "suspicious_keyword",
        "suspicious_keyword",
        "suspicious_keyword",
    ]

    score, _ = calculate_score(flags)

    assert score <= 100