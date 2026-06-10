# 🛡️ SecureInspect

A lightweight Python-based cybersecurity toolkit for security analysis, monitoring, and threat detection.

---

## 🔧 Available Tools

### 1. QR Code Safety Scanner

A security-focused tool that analyzes QR code content and identifies potentially malicious or unsafe patterns.

It identifies:

- Non-HTTPS URLs  
- URL shorteners  
- IP-based URLs  
- Suspicious top-level domains (TLDs)  
- Phishing-related keywords  

Each scanned QR code is evaluated and assigned a **risk score** along with a **safety status**.

---

### 2. File Integrity Checker

A File Integrity Monitoring (FIM) tool that uses **SHA-256 hashing** to detect file tampering or unauthorized modifications.

It compares a trusted baseline against the current state of files to detect:

- New files  
- Deleted files  
- Modified files  

It also generates **JSON and TXT reports** containing:

- Detected changes  
- Risk score  
- Integrity status  

---

## 📁 Repository Structure

```text
SecureInspect/
│
├── qr-code-safety-scanner/
│
└── file-integrity-checker/
```

---

## 📌 Note

Each tool includes its own README with setup instructions, usage examples, and implementation details.

