Sure! Here is a complete, polished `README.md` file you can copy and paste directly into your project:


# ⚡ Python Multithreaded Port Scanner

A high-speed multithreaded port scanner written in Python. This tool scans a given IP address for open ports using concurrent threads to improve scanning performance.

---

## 🔧 Features

- Multithreaded scanning with configurable number of threads (default: 500)
- Scan custom port ranges or all ports (0-65535)
- Real-time progress indicator during scanning
- Identifies and lists open ports
- Simple terminal interface with banner

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x (tested with Python 3.7+)
- No external dependencies (uses only built-in Python libraries)

---

### 🛠️ How to Use

Run the script in your terminal or command prompt:

```bash
python port_scanner.py
````

You will be prompted to enter:

* Target IP address (e.g., `192.168.1.151`)
* Port range in the format `start-end` (e.g., `0-1024`)
  Or type `0` to scan all ports from 0 to 65535.

---

### 📦 Example

```bash
What’s the target s IP ADDRESS: 192.168.1.151
Enter a port range in this format start-end or type 0 to scan all ports: 0
```

Sample output:

```
[⏳] Ports scanned: 14503
[!] Port 55442 is OPEN
[!] Port 8009 is OPEN
[✔] Scanned ports 0-65535 in 132.82 seconds.
```

---

## 🧠 How It Works

* The port range is divided into chunks assigned to multiple threads (default 500).
* Each thread scans its chunk of ports in parallel using socket connections with a timeout.
* Open ports are detected by successful connections.
* Progress is shown as ports are scanned.
* Open ports are collected and displayed after scanning completes.

---

## ⚠️ Legal Disclaimer

> This tool is intended **for educational purposes and authorized security testing only**.
> Unauthorized port scanning of systems you do not own or have explicit permission to test is illegal and unethical.
> The author assumes no responsibility for misuse of this software.



---

## 💻 Author

**R4Y** – [GitHub Profile](https://github.com/r4y-br)

---

Feel free to open issues or submit pull requests if you want to contribute!
