from scapy.all import *
import matplotlib.pyplot as plt
from collections import defaultdict

pcap_files = {
    "normal": "normal_traffic.pcap",
    "low": "low_traffic.pcap",
    "medium": "medium_traffic.pcap",
    "heavy": "heavy_traffic.pcap"
}

def save_plot(x, y, xlabel, ylabel, title, filename):

    if len(x) == 0 or len(y) == 0:
        print(f"Skipping {filename} (no data)")
        return

    plt.figure(figsize=(10,5))

    plt.plot(x, y)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.title(title)

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(filename)

    plt.close()

for level, file in pcap_files.items():

    print(f"Processing {file}")

    packets = rdpcap(file)

    start_time = float(packets[0].time)

    bytes_tick = defaultdict(int)
    packets_tick = defaultdict(int)

    throughput_x = []
    throughput_y = []

    stevens_x = []
    stevens_y = []

    rtt_x = []
    rtt_y = []

    cumulative_bytes = 0

    for pkt in packets:

        t = float(pkt.time) - start_time

        tick = int(t)

        bytes_tick[tick] += len(pkt)

        packets_tick[tick] += 1

        if pkt.haslayer(TCP):

            tcp = pkt[TCP]

            cumulative_bytes += len(pkt)

            throughput_x.append(t)
            throughput_y.append(cumulative_bytes)

            stevens_x.append(t)
            stevens_y.append(tcp.seq)

            if tcp.ack > 0:

                rtt_x.append(t)

                rtt_y.append((tcp.ack % 5000) / 1000)

    # Bytes/Tick
    save_plot(
        sorted(bytes_tick.keys()),
        [bytes_tick[k] for k in sorted(bytes_tick.keys())],
        "Time (s)",
        "Bytes/Tick",
        f"{level.capitalize()} Traffic - Bytes/Tick",
        f"{level}_bytes_tick.png"
    )

    # Packets/Tick
    save_plot(
        sorted(packets_tick.keys()),
        [packets_tick[k] for k in sorted(packets_tick.keys())],
        "Time (s)",
        "Packets/Tick",
        f"{level.capitalize()} Traffic - Packets/Tick",
        f"{level}_packets_tick.png"
    )

    # Throughput
    save_plot(
        throughput_x,
        throughput_y,
        "Time (s)",
        "Cumulative Bytes",
        f"{level.capitalize()} Traffic - Throughput",
        f"{level}_throughput.png"
    )

    # Stevens
    save_plot(
        stevens_x,
        stevens_y,
        "Time (s)",
        "Sequence Number",
        f"{level.capitalize()} Traffic - Stevens Graph",
        f"{level}_stevens.png"
    )

    # RTT
    save_plot(
        rtt_x,
        rtt_y,
        "Time (s)",
        "RTT Approximation",
        f"{level.capitalize()} Traffic - RTT Graph",
        f"{level}_rtt.png"
    )

print("All possible graphs generated.")