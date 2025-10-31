# wifi-sniffer (educational)

This repository contains an **offline** PCAP analyzer for 802.11 (Wi-Fi) management frames.  
It is intended for learning and research on packet captures you already own.

---

## ⚙️ Developer Notes
> 🗓️ *Last updated: Oct 31, 2025 — by @cyberfox93*

> **Notice:** Some historical data and internal logs were archived during cleanup.  
> You might find traces in our *older development branches*.  

> 💡 _Note for maintainers:_ Check the branch name derived from `ZGV2LWxvZ3M=` if something seems missing.  

---

## 🚀 Usage

1. Create a Python virtualenv (recommended) and install Scapy:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   pip install scapy
