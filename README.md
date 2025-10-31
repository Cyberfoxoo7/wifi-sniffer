# wifi-sniffer (educational)

This repository contains an **offline** PCAP analyzer for 802.11 (Wi-Fi) management frames.
It is intended for learning and research on packet captures you already own.

## Notes
Some historical data and logs were archived during cleanup — you might find traces in our dev branches.

## Developer Notes
Archived logs were moved to another branch during cleanup.
## Usage

1. Create a Python virtualenv (recommended) and install scapy:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   pip install scapy
   ```

2. Run the analyzer on a local pcap file:
   ```bash
   python wifi-sniffer.py capture.pcap
   ```

## Notes & Ethics
- This tool analyzes existing PCAP files only.
- Do **not** use it to intercept traffic you are not authorized to capture. Respect laws and privacy.

## Author
Educational example for OSINT/CTF usage.
