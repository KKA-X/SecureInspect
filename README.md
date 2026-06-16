# 🛡️ SecureInspect

A lightweight Python-based cybersecurity toolkit for security analysis, monitoring, and threat detection.

---

## 🔧 Available Tools

### 1. QR Code Safety Scanner

A security-focused tool that analyzes QR code content and identifies potentially malicious or unsafe patterns.

It identifies:

* Non-HTTPS URLs
* URL shorteners
* IP-based URLs
* Suspicious top-level domains (TLDs)
* Phishing-related keywords

Each scanned QR code is evaluated and assigned a **risk score** along with a **safety status**.

---

### 2. File Integrity Checker

A File Integrity Monitoring (FIM) tool that uses **SHA-256 hashing** to detect file tampering or unauthorized modifications.

It compares a trusted baseline against the current state of files to detect:

* New files
* Deleted files
* Modified files

It also generates **JSON and TXT reports** containing:

* Detected changes
* Risk score
* Integrity status

---

### 3. GhostGlyph

A Unicode security scanner that detects hidden Unicode characters and homoglyph-based spoofing attacks commonly used in phishing, social engineering, text obfuscation, and Unicode abuse attacks.

It identifies:

* Invisible Unicode characters
* Zero-width characters
* Bidirectional text override characters
* Unicode formatting controls
* Homoglyph spoofing attacks

It also generates **JSON and CSV reports** containing detected findings.

---

## 🚀 Current Toolkit Overview

| Tool                   | Purpose                                                       |
| ---------------------- | ------------------------------------------------------------- |
| QR Code Safety Scanner | Detects potentially unsafe or malicious QR code content       |
| File Integrity Checker | Detects unauthorized file changes using SHA-256 hashing       |
| GhostGlyph             | Detects hidden Unicode threats and homoglyph spoofing attacks |

---

## 📁 Repository Structure

```text
SecureInspect/
│
├── qr-code-safety-scanner/
│
├── file-integrity-checker/
│
└── ghostglyph/
```

---

## 📌 Note

Each tool includes its own README containing:

* Installation instructions
* Usage examples
* Project structure
* Testing information
* Technical implementation details

Refer to the individual tool directories for complete documentation.
