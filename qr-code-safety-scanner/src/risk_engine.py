def calculate_score(flags):
    score = 0

    penalties = {
        "non_https": 20,
        "shortener": 25,
        "ip_url": 30,
        "suspicious_tld": 15,
        "suspicious_keyword": 10,
    }

    for flag in flags:
        score += penalties.get(flag, 0)

    score = min(score, 100)

    if score <= 0:
        level = "SAFE"
    elif score <= 50:
        level = "MEDIUM"
    else:
        level = "HIGH RISK"

    return score, level