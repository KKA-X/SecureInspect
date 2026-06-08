from src.analyzer import analyze


def test_very_long_url():
    url = "https://example.com/" + "a" * 5000

    result = analyze(url)

    assert isinstance(result, dict)


def test_uppercase_url():
    result = analyze("HTTPS://EXAMPLE.COM")

    assert result["content"] == "HTTPS://EXAMPLE.COM"


def test_mixed_case_keyword():
    result = analyze("https://example.com/LoGiN")

    assert any("login" in warning.lower() for warning in result["warnings"])


def test_local_ip():
    result = analyze("http://127.0.0.1")

    assert "IP Address URL" in result["warnings"]


def test_private_ip():
    result = analyze("http://192.168.1.100")

    assert "IP Address URL" in result["warnings"]