# 🔍 Port Scanner

A simple yet powerful **Python-based Port Scanner** that scans open ports on a given IP address or domain. Ideal for ethical hacking labs, penetration testing practice, and learning how TCP/UDP ports work.

---

## 📌 Features

- Scan a **range of ports** (e.g., 1–1000)
- Identify **open ports**
- Support for **domain names** and **IP addresses**
- Clear, colored console output
- Easy to use via command line

---

## 🚀 How It Works

The script uses Python’s built-in `socket` library to:
- Attempt to connect to each port on the target IP.
- Report which ports are open.
- Time out inactive ports after 1 second (to keep scanning fast).

---

## 🧪 Example

```bash
Enter the IP address or hostname to scan: 192.168.1.1
Enter the range of ports to scan (e.g., 1-500): 1-100

Scanning 192.168.1.1 for open ports from 1 to 100...

[+] Port 22 is open
[+] Port 80 is open

Scan completed in 3.42 seconds.
