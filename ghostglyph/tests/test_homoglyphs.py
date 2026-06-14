from ghostglyph.homoglyphs import find_homoglyphs

def test_homoglyph_detection():

    text = "gοοgle"

    findings = find_homoglyphs(text)

    assert len(findings) == 2

    assert findings[0]["character"] == "ο"
    assert findings[0]["looks_like"] == "o"

    assert findings[0]["risk"] == "HIGH"
    assert findings[0]["type"] == "homoglyph"

def test_clean_text():

    text = "google"

    findings = find_homoglyphs(text)

    assert findings == []

def test_multiple_homoglyph_types():

    text = "раураl"

    findings = find_homoglyphs(text)

    assert len(findings) > 0