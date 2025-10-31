#!/usr/bin/env python3
"""wifi-sniffer (educational) — offline pcap analyzer

This script reads a pcap (packet capture) file and summarizes Wi-Fi (802.11)
management frames found in the file.

Usage:
    python wifi-sniffer.py capture.pcap
"""

import sys
from collections import Counter

try:
    from scapy.all import rdpcap, Dot11
except Exception:
    print("scapy is required. Install with: pip install scapy")
    sys.exit(1)

def summarize_pcap(path):
    packets = rdpcap(path)
    ssids = Counter()
    beacons = 0
    probes = 0

    for pkt in packets:
        if Dot11 in pkt:
            try:
                # type 0 = management frames; subtype 8 = Beacon, 4 = Probe Request
                if pkt.type == 0 and pkt.subtype == 8:  # beacon
                    beacons += 1
                    # pkt.info is the SSID field for beacon/probe response
                    if hasattr(pkt, 'info') and pkt.info:
                        ssid = pkt.info.decode(errors='ignore').strip()
                        if ssid:
                            ssids[ssid] += 1
                elif pkt.type == 0 and pkt.subtype == 4:  # probe request
                    probes += 1
            except Exception:
                # ignore malformed packet decode errors
                pass

    print(f"Total frames analyzed: {len(packets)}")
    print(f"Beacon frames: {beacons}")
    print(f"Probe request frames: {probes}")
    print("Top SSIDs observed:")
    for ssid, count in ssids.most_common(10):
        print(f"  {ssid!r}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wifi-sniffer.py capture.pcap")
        sys.exit(1)
    summarize_pcap(sys.argv[1])
