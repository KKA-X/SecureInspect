from pathlib import Path
from .homoglyphs import find_homoglyphs

SUSPICIOUS_UNICODE = {
    "\u200B": ("ZERO WIDTH SPACE", "HIGH"),
    "\u200C": ("ZERO WIDTH NON-JOINER", "HIGH"),
    "\u200D": ("ZERO WIDTH JOINER", "HIGH"),
    "\u2060": ("WORD JOINER", "MEDIUM"),
    "\uFEFF": ("ZERO WIDTH NO-BREAK SPACE", "HIGH"),
    "\u202E": ("RIGHT TO LEFT OVERRIDE", "CRITICAL"),
    "\u202D": ("LEFT TO RIGHT OVERRIDE", "CRITICAL"),
    "\u202A": ("LEFT TO RIGHT EMBEDDING", "HIGH"),
    "\u202B": ("RIGHT TO LEFT EMBEDDING", "HIGH"),
    "\u202C": ("POP DIRECTIONAL FORMATTING", "HIGH"),
}

def scan_text(text):
    findings = []

    for pos, char in enumerate(text):

        if char in SUSPICIOUS_UNICODE:

            name, risk = SUSPICIOUS_UNICODE[char]

            findings.append({
                "position": pos,
                "character": char,
                "unicode": f"U+{ord(char):04X}",
                "name": name,
                "risk": risk,
                "type": "unicode"
            })

    for item in find_homoglyphs(text):

        if item not in findings:
            findings.append(item)

    return findings

def scan_file(path):

    content = (
        Path(path)
        .expanduser()
        .read_text(
            encoding="utf-8",
            errors="replace"
        )
    )

    return scan_text(content)

def calculate_risk_score(findings):

    score = 0

    for item in findings:

        risk = item.get("risk")
        item_type = item.get("type")

        if risk == "CRITICAL":
            score += 40

        elif risk == "HIGH":
            score += 20

        elif risk == "MEDIUM":
            score += 10

        elif item_type == "homoglyph":
            score += 15

    return min(score, 100)

def summarize(findings):

    return {
        "count": len(findings),
        "risk_score": calculate_risk_score(findings)
    }