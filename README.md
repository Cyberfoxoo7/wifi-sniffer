# wifi-sniffer (educational)

This repository contains an **offline** PCAP analyzer for 802.11 (Wi-Fi) management frames.  
It is intended for learning and research on packet captures you already own.

---

## Developer Notes
Archived logs were moved to another branch during cleanup.  

> 🧠 *Note for maintainers:*  
> Some commits reference `ZGV2LWxvZ3M=` — decode if unsure which branch to check.  
> Legacy notes may contain internal tags wrapped in `NFSU{}`.

---

## 🚀 Usage

1. Create a Python virtualenv (recommended) and install Scapy:
   ```bash
   python -m venv venv
   source venv/bin/activate     # Windows: venv\Scripts\activate
   pip install scapy
