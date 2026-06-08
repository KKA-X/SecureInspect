from src.analyzer import analyze


def test_https_safe():
    result = analyze("https://example.com")

    assert result["risk_score"] == 0
    assert result["risk_level"] == "SAFE"
    assert result["warnings"] == []


def test_http_url():
    result = analyze("http://example.com")

    assert "Non-HTTPS URL" in result["warnings"]
    assert result["risk_score"] > 0


def test_shortener_bitly():
    result = analyze("https://bit.ly/test")

    assert "URL Shortener Detected" in result["warnings"]
    assert result["risk_score"] > 0


def test_shortener_tinyurl():
    result = analyze("https://tinyurl.com/test")

    assert "URL Shortener Detected" in result["warnings"]
    assert result["risk_score"] > 0


def test_ip_address_url():
    result = analyze("http://192.168.1.1")

    assert "IP Address URL" in result["warnings"]
    assert result["risk_score"] > 0


def test_suspicious_tld_xyz():
    result = analyze("https://fake.xyz")

    assert "Suspicious TLD" in result["warnings"]
    assert result["risk_score"] > 0


def test_suspicious_tld_top():
    result = analyze("https://fake.top")

    assert "Suspicious TLD" in result["warnings"]
    assert result["risk_score"] > 0


def test_login_keyword():
    result = analyze("https://example.com/login")

    assert any("login" in warning.lower() for warning in result["warnings"])


def test_verify_keyword():
    result = analyze("https://example.com/verify")

    assert any("verify" in warning.lower() for warning in result["warnings"])


def test_password_keyword():
    result = analyze("https://example.com/password")

    assert any("password" in warning.lower() for warning in result["warnings"])


def test_reward_keyword():
    result = analyze("https://example.com/reward")

    assert any("reward" in warning.lower() for warning in result["warnings"])


def test_gift_keyword():
    result = analyze("https://example.com/gift")

    assert any("gift" in warning.lower() for warning in result["warnings"])


def test_update_account_keyword():
    result = analyze("https://example.com/update-account")

    assert any("update-account" in warning.lower() for warning in result["warnings"])


def test_plain_text():
    result = analyze("Hello World")

    assert result["risk_score"] == 0
    assert result["risk_level"] == "SAFE"


def test_empty_string():
    result = analyze("")

    assert result["risk_score"] == 0
    assert result["risk_level"] == "SAFE"


def test_multiple_risks_ip_and_http():
    result = analyze("http://192.168.1.1/login")

    assert "Non-HTTPS URL" in result["warnings"]
    assert "IP Address URL" in result["warnings"]

    assert any("login" in warning.lower() for warning in result["warnings"])

    assert result["risk_score"] > 0


def test_multiple_risks_shortener_and_keyword():
    result = analyze("http://bit.ly/login")

    assert "Non-HTTPS URL" in result["warnings"]
    assert "URL Shortener Detected" in result["warnings"]

    assert any("login" in warning.lower() for warning in result["warnings"])

    assert result["risk_score"] > 0


def test_multiple_risks_tld_and_keyword():
    result = analyze("http://fake.xyz/login")

    assert "Non-HTTPS URL" in result["warnings"]
    assert "Suspicious TLD" in result["warnings"]

    assert any("login" in warning.lower() for warning in result["warnings"])

    assert result["risk_score"] > 0


def test_content_field_preserved():
    url = "https://example.com"

    result = analyze(url)

    assert result["content"] == url


def test_return_structure():
    result = analyze("https://example.com")

    assert "content" in result
    assert "risk_score" in result
    assert "risk_level" in result
    assert "warnings" in result