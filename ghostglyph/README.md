# SecureInspect - GhostGlyph

A lightweight Python-based Unicode security scanner that detects hidden Unicode characters and homoglyph-based spoofing attacks commonly used in phishing, social engineering, text obfuscation, and Unicode abuse attacks.

GhostGlyph scans text files and identifies:

* Invisible Unicode characters
* Zero-width characters
* Bidirectional text override characters
* Unicode formatting controls
* Homoglyph spoofing attacks

It can also export findings as JSON and CSV reports for further analysis.

---

## Features

* Invisible Unicode detection
* Zero-width character detection
* Bidirectional override detection
* Unicode formatting control detection
* Homoglyph attack detection
* Risk scoring system
* JSON report generation
* CSV report generation
* Colored terminal output
* Automated testing with Pytest

---

## What is a Unicode Spoofing Attack?

Unicode spoofing attacks use special Unicode characters to hide malicious content or make text appear different from its actual value.

These techniques are commonly used in:

* Phishing attacks
* Social engineering
* Username spoofing
* Domain impersonation
* Source code obfuscation
* Hidden text injection

---

### Hidden Character Example

Normal text:

```text
admin
```

Text containing an invisible Unicode character:

```text
ad​min
```

The hidden character is:

```text
U+200B ZERO WIDTH SPACE
```

Although both strings look similar, they are not identical.

---

### Homoglyph Attack Example

Legitimate text:

```text
google
```

Spoofed text:

```text
gοοgle
```

The highlighted characters are Greek letters that visually resemble the English letter:

```text
o
```

This technique can be used to deceive users into trusting malicious content.

---

## Detection Workflow

```text
Input File
      ↓
Read Content
      ↓
Scan Unicode Characters
      ↓
Scan Homoglyph Characters
      ↓
Calculate Risk
      ↓
Generate Report
```

---

## Project Structure

```text
ghostglyph/
│
├── ghostglyph/
│   ├── __init__.py
│   ├── cli.py
│   ├── homoglyphs.py
│   ├── reporters.py
│   └── scanner.py
│
├── samples/
│   ├── clean.txt
│   ├── homoglyph_attack.txt
│   └── unicode_attack.txt
│
├── tests/
│   ├── test_homoglyphs.py
│   └── test_scanner.py
│
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

---

## Requirements

* Python 3.10 or later
* Linux, Windows, or macOS

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/KKA-X/SecureInspect.git
cd SecureInspect/ghostglyph
```

### 2. Create a Virtual Environment

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install GhostGlyph

```bash
pip install -e .
```

---

## Verify Installation

```bash
ghostglyph --help
```

Example output:

```text
usage: ghostglyph [-h] [--json JSON] [--csv CSV] target
```

---

## Basic Usage

Scan a file:

```bash
ghostglyph samples/unicode_attack.txt
```

Example output:

```text
========================================
      GhostGlyph Security Scanner
   Invisible Unicode Threat Detector
========================================

File Scanned : unicode_attack.txt
Threats Found: 1

----------------------------------------
[HIGH] Unicode Threat Detected
Location : 2
Codepoint: U+200B
Name     : ZERO WIDTH SPACE

========================================
[SUMMARY]
Total Threats: 1
```

---

## Export JSON Report

```bash
ghostglyph samples/unicode_attack.txt --json report.json
```

Example output:

```text
========================================
      GhostGlyph Security Scanner
   Invisible Unicode Threat Detector
========================================

File Scanned : unicode_attack.txt
Threats Found: 1

----------------------------------------
[HIGH] Unicode Threat Detected
Location : 2
Codepoint: U+200B
Name     : ZERO WIDTH SPACE

========================================
[SUMMARY]
Total Threats: 1

[OK] JSON exported → /path/to/report.json
```

Generated report:

```json
[
    {
        "position": 2,
        "character": "​",
        "unicode": "U+200B",
        "name": "ZERO WIDTH SPACE",
        "risk": "HIGH",
        "type": "unicode"
    }
]
```

---

## Export CSV Report

```bash
ghostglyph samples/unicode_attack.txt --csv report.csv
```

Example output:

```text
========================================
      GhostGlyph Security Scanner
   Invisible Unicode Threat Detector
========================================

File Scanned : unicode_attack.txt
Threats Found: 1

----------------------------------------
[HIGH] Unicode Threat Detected
Location : 2
Codepoint: U+200B
Name     : ZERO WIDTH SPACE

========================================
[SUMMARY]
Total Threats: 1

[OK] CSV exported → /path/to/report.csv
```

Generated report:

```csv
position,character,unicode,name,risk,type
2,,U+200B,ZERO WIDTH SPACE,HIGH,unicode
```

---

## Supported Unicode Threats

| Unicode Character | Description                | Risk Level |
| ----------------- | -------------------------- | ---------- |
| U+200B            | Zero Width Space           | HIGH       |
| U+200C            | Zero Width Non-Joiner      | HIGH       |
| U+200D            | Zero Width Joiner          | HIGH       |
| U+2060            | Word Joiner                | MEDIUM     |
| U+FEFF            | Zero Width No-Break Space  | HIGH       |
| U+202E            | Right-To-Left Override     | CRITICAL   |
| U+202D            | Left-To-Right Override     | CRITICAL   |
| U+202A            | Left-To-Right Embedding    | HIGH       |
| U+202B            | Right-To-Left Embedding    | HIGH       |
| U+202C            | Pop Directional Formatting | HIGH       |

---

## Running Tests

Run all tests:

```bash
python -m pytest -v
```

Example output:

```text
9 passed
```

The test suite verifies:

* Unicode threat detection
* Zero-width character detection
* Bidirectional override detection
* Homoglyph detection
* Multiple homoglyph type detection
* Risk score calculation
* Empty input handling
* Mixed threat detection
* Clean text scanning

---

## Error Handling

The tool handles:

* Missing files
* Invalid file paths
* UTF-8 decoding issues
* Empty input files
* Report export generation

---

## Technologies Used

* Python
* Unicode Character Analysis
* Colorama
* Pytest

---

## License

This project is licensed under the MIT License.

See the LICENSE file for details.
