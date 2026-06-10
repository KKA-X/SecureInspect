# SecureInspect - File Integrity Checker

A lightweight Python-based File Integrity Monitoring (FIM) tool that uses SHA-256 hashing to detect unauthorized file changes.

The tool creates a trusted baseline of file hashes and later compares the current state of a directory against that baseline to identify:

* New files
* Deleted files
* Modified files

It also generates detailed JSON and TXT reports containing detected file changes, risk scores, and integrity assessment results.

---

## Features

* SHA-256 file hashing
* Baseline creation
* File integrity verification
* Detect new files
* Detect deleted files
* Detect modified files
* Risk score calculation
* JSON report generation
* TXT report generation
* Rich terminal interface
* Automated testing with Pytest

---

## What is File Integrity Monitoring?

File Integrity Monitoring (FIM) is a security technique used to detect unauthorized file changes by comparing the current state of files against a trusted baseline.

Workflow:

```text
Create Baseline
       ↓
Store File Hashes
       ↓
Scan Directory
       ↓
Compare Hashes
       ↓
Detect New, Deleted, or Modified Files
```

This project uses SHA-256 hashing to identify changes and generate a simple risk assessment report.

---

## Project Structure

```text
file-integrity-checker/
│
├── samples/
│   ├── file1.txt
│   └── file2.txt
│
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── baseline_manager.py
│   ├── hashing.py
│   ├── integrity_checker.py
│   └── report_generator.py
│
├── tests/
│   ├── test_analyzer.py
│   ├── test_hashing.py
│   └── test_report_generator.py
│
├── LICENSE
├── .gitignore
├── pytest.ini
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
cd SecureInspect/file-integrity-checker
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

## Creating a Baseline

Before monitoring files, create a trusted baseline.

Example:

```bash
python src/integrity_checker.py --create samples
```

Successful output:

```text
✓ Baseline Created Successfully
```

This creates:

```text
baseline.json
```

which stores the SHA-256 hashes of all files in the selected directory.

---

## Verifying File Integrity

Run verification against the previously created baseline.

Example:

```bash
python src/integrity_checker.py --verify samples
```

The tool will:

1. Load the baseline
2. Scan the directory
3. Calculate new hashes
4. Compare hashes
5. Detect changes
6. Generate reports

---

## Sample Output

```text
SecureInspect
File Integrity Checker

New Files       : 0
Deleted Files   : 0
Modified Files  : 0
Risk Score      : 0
Status          : SAFE
```

---

## Risk Scoring

The tool assigns a risk score based on detected changes.

| Event         | Score |
| ------------- | ----- |
| New File      | +10   |
| Deleted File  | +20   |
| Modified File | +25   |

Maximum score:

```text
100
```

---

## Risk Levels

| Score    | Status             |
| -------- | ------------------ |
| 0        | SAFE               |
| 1 - 50   | ATTENTION REQUIRED |
| 51 - 100 | HIGH RISK          |

---

## Generated Reports

After verification, the following reports are generated.

### integrity_report.json

Machine-readable report.

Example:

```json
{
    "report": {
        "new_files": [],
        "deleted_files": [],
        "modified_files": []
    },
    "risk_score": 0,
    "status": "SAFE"
}
```

---

### integrity_report.txt

Human-readable report.

Example:

```text
FILE INTEGRITY REPORT
========================================

Risk Score: 0
Status: SAFE
```

---

## Running Tests

Run all tests:

```bash
pytest -v
```

Example output:

```text
15 passed
```

The test suite verifies:

* SHA-256 hash generation
* Hash consistency
* Hash uniqueness
* Empty file hashing
* New file detection
* Deleted file detection
* Modified file detection
* Risk score calculation
* JSON report generation
* TXT report generation

---

## Error Handling

The tool handles:

* Missing baseline files
* Invalid directories
* File access errors
* File hashing failures

---

## Technologies Used

* Python
* SHA-256 (hashlib)
* Rich
* Pytest

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
