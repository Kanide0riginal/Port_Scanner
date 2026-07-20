**Port Scanner**
A simple TCP port scanner written in Python.

**What it does**
Scans a range of ports on a target IP or hostname and reports which ones are open, along with the service name where known.

How to run
```bash
python port_scanner.py
```

You will be prompted to enter:
- Target IP or hostname (e.g. `127.0.0.1`)
- Start port (e.g. `1`)
- End port (e.g. `1024`)

Sample Output
```
Scanning 127.0.0.1 (127.0.0.1)
Ports 1-1024 | Started at 2026-07-12 13:35:23.825891
```
| Port | Status | Service |
|------|--------|---------|
| 135 | OPEN | epmap |
| 445 | OPEN | microsoft-ds |
| 902 | OPEN | unknown |
| 912 | OPEN | unknown |

**Scan complete:** 4 open ports found.

**What I Learned**
- Open ports represent potential attack surfaces on any system.
- Port **445 (SMB)** is historically one of the most targeted ports and was exploited by the WannaCry ransomware in 2017.
- Port **135 (RPC)** is commonly abused for lateral movement in Windows environments.
- Reconnaissance (port scanning) is the first phase of many penetration tests.

**Skills Demonstrated**
- Python socket programming
- TCP connection handling
- Network reconnaissance fundamentals
- Error handling and timeout management

Author: Kanishk Khobragade
# Port_Scanner
A simple TCP port scanner written in Python.
