import re
from urllib.parse import urlparse
from src.risk_engine import calculate_score

SHORTENERS = {"bit.ly","tinyurl.com","t.co","is.gd","ow.ly","buff.ly"}
SUSPICIOUS_TLDS = {".xyz",".top",".click",".loan",".gq"}
KEYWORDS = ["login","verify","password","reward","gift","update-account"]

def analyze(content):
    flags = []
    warnings = []

    if content.startswith(("http://","https://")):
        parsed = urlparse(content)
        host = parsed.hostname or ""

        if parsed.scheme != "https":
            flags.append("non_https")
            warnings.append("Non-HTTPS URL")

        if host.lower() in SHORTENERS:
            flags.append("shortener")
            warnings.append("URL Shortener Detected")

        if re.match(r"^\d+\.\d+\.\d+\.\d+$", host):
            flags.append("ip_url")
            warnings.append("IP Address URL")

        for tld in SUSPICIOUS_TLDS:
            if host.endswith(tld):
                flags.append("suspicious_tld")
                warnings.append("Suspicious TLD")
                break

        lower = content.lower()
        for k in KEYWORDS:
            if k in lower:
                flags.append("suspicious_keyword")
                warnings.append(f"Suspicious Keyword: {k}")

    score, level = calculate_score(flags)

    return {
        "content": content,
        "risk_score": score,
        "risk_level": level,
        "warnings": warnings
    }
