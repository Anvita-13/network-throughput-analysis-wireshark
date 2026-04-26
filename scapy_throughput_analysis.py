from scapy.all import rdpcap
from collections import Counter

packets = rdpcap("heavy_traffic.pcapng")

print("Total packets:", len(packets))

src_ips = set()
dst_ips = set()
protocols = []

for pkt in packets:
    if pkt.haslayer("IP"):
        src_ips.add(pkt["IP"].src)
        dst_ips.add(pkt["IP"].dst)
        protocols.append(pkt["IP"].proto)

print("Unique source IPs:", len(src_ips))
print("Unique destination IPs:", len(dst_ips))

count = Counter(protocols)

print("Protocols used:")

for proto, num in count.items():
    print(f"Protocol {proto}: {num} packets")