# SecureInspect - QR Code Safety Scanner

A lightweight Python-based security tool that analyzes QR code content and identifies potentially suspicious indicators such as non-HTTPS links, URL shorteners, IP-based URLs, suspicious top-level domains (TLDs), and phishing-related keywords.

The scanner extracts data from QR codes, evaluates security risks, generates a risk score, and produces detailed reports in both JSON and TXT formats.

---

## Features

* Decode QR codes from images
* Detect non-HTTPS URLs
* Detect URL shorteners
* Detect IP address URLs
* Detect suspicious TLDs
* Detect phishing-related keywords
* Calculate risk scores automatically
* Generate security reports
* Terminal-based user interface using Rich
* Automated test suite using Pytest

---

## Project Structure

```text
qr-code-safety-scanner/
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── risk_engine.py
│   ├── scanner.py
│   └── report_generator.py
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_edge_cases.py
│   ├── test_risk_engine.py
│   └── test_scanner_flow.py
│
├── samples/
│   ├── qr1.png
│   ├── qr2.png
│   ├── qr3.png
│   ├── qr4.png
│   ├── qr5.png
│   ├── qr6.png
│   ├── qr7.png
│   └── qr8.png
│
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
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
cd SecureInspect/qr-code-safety-scanner
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

---

## Running the Scanner

Basic Usage:

```bash
python -m src.scanner <image_path>
```

Example:

```bash
python -m src.scanner samples/QR1.png
```

---

## Sample Output

```text
SecureInspect
QR Code Safety Scanner

Content    : https://www.google.com/
Risk Score : 0
Risk Level : SAFE
```

---

## Generated Reports

After every successful scan, the following files are generated:

### report.json

Contains machine-readable scan results.

### report.txt

Contains a human-readable scan report.

---

## Risk Indicators

The scanner currently checks for:

### Non-HTTPS URLs

Example:

```text
http://example.com
```

### URL Shorteners

Examples:

```text
https://bit.ly/example
https://tinyurl.com/example
```

### IP Address URLs

Example:

```text
http://192.168.1.1
```

### Suspicious Top-Level Domains

Examples:

```text
.xyz
.top
.click
.loan
.gq
```

### Suspicious Keywords

Examples:

```text
login
verify
password
reward
gift
update-account
```

---

## Risk Levels

| Score    | Level     |
| -------- | --------- |
| 0        | SAFE      |
| 1 - 50   | MEDIUM    |
| 51 - 100 | HIGH RISK |

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Expected output:

```text
31 passed
```

The test suite verifies:

* URL analysis
* Risk scoring
* Edge cases
* Report generation
* Scanner workflow

---

## Error Handling

The scanner handles:

* Missing image files
* Invalid image formats
* Images without QR codes
* Suspicious QR content
* Multiple risk indicators

---

## Technologies Used

* Python
* OpenCV
* Pyzbar
* Rich
* Pytest

---

## Disclaimer

This project is intended for educational and defensive security purposes. The risk score is heuristic-based and should not be considered a definitive security assessment.

---

## License

This project is licensed under the MIT License.
See the LICENSE file for details.
