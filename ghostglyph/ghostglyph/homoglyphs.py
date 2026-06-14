"""
Common homoglyph mappings used in phishing and spoofing attacks.
"""

HOMOGLYPHS = {
    # Cyrillic
    "а": "a",
    "е": "e",
    "о": "o",
    "р": "p",
    "с": "c",
    "х": "x",
    "у": "y",

    # Greek
    "Α": "A",
    "Β": "B",
    "Ε": "E",
    "Ζ": "Z",
    "Η": "H",
    "Ι": "I",
    "Κ": "K",
    "Μ": "M",
    "Ν": "N",
    "Ο": "O",
    "Ρ": "P",
    "Τ": "T",
    "Χ": "X",

    "ο": "o",
    "ι": "i",
    "ρ": "p",
}

def find_homoglyphs(text):

    findings = []

    for pos, char in enumerate(text):

        if char in HOMOGLYPHS:

            findings.append({
                "position": pos,
                "character": char,
                "looks_like": HOMOGLYPHS.get(char),
                "risk": "HIGH",
                "type": "homoglyph"
            })

    return findings