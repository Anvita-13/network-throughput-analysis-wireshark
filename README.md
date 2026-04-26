# Network Throughput Analysis Using Wireshark

## Overview

This project presents a detailed analysis of network throughput using Wireshark under controlled traffic conditions. The study was carried out to understand how throughput behaves in real network environments and how it varies with different traffic intensities.

The experiment involves generating traffic using command-based tools and analyzing packet captures through various Wireshark graphs such as I/O graphs, TCP throughput graphs, and TCP Time-Sequence (Stevens) graphs.

---

## Objectives

- To understand throughput as a practical network performance parameter  
- To analyze network behavior using Wireshark  
- To measure throughput under different traffic conditions  
- To interpret throughput using graphical analysis  
- To study TCP behavior and its impact on throughput  

---

## Tools and Technologies Used

- Wireshark (Packet Capture and Analysis)
- Scapy (Packet Inspection and Traffic Analysis)  
- hping3 (Traffic Generation Tool)  
- GitHub (Repository Management)  

---

## Traffic Conditions

Traffic was generated under four different conditions:

- Normal Traffic  
- Low Traffic  
- Medium Traffic  
- High Traffic  

All traffic was generated using controlled command execution without flooding or browser-based methods.

---

## Traffic Generation Commands

Normal Traffic:
    sudo hping3 google.com -S -p 80 -i u500000 -c 120

Low Traffic:
    sudo hping3 google.com -S -p 80 -i u100000 -c 300

Medium Traffic:
    sudo hping3 google.com -S -p 80 -i u50000 -c 600

High Traffic:
    sudo hping3 google.com -S -p 80 -i u10000 -c 1000

---

## Methodology

1. Start Wireshark and select the active network interface  
2. Begin packet capture  
3. Execute traffic generation command  
4. Allow capture to complete  
5. Stop capture and save `.pcap` file  
6. Apply filters (e.g., `tcp`)  
7. Generate graphs using Wireshark tools  
8. Analyze and interpret results  
9. Perform supplementary packet inspection using Scapy scripts  

---

## Analysis Performed

- I/O Graphs (Bytes/Tick and Packets/Tick)  
- TCP Throughput Graphs  
- TCP Time-Sequence (Stevens) Graphs  
- RTT Graphs  
- Scapy-based packet inspection and protocol analysis  

A total of 20 graphs were generated across different traffic levels.

---

## Key Observations

- Throughput increases with traffic intensity  
- I/O graphs clearly show variation in network activity  
- TCP behavior becomes more irregular under high traffic  
- Stevens graphs show sequence number progression over time  
- RTT variation increases with higher traffic load  

---

## Repository Contents

- Packet capture files (`.pcap`)  
- Graph screenshots  
- Architecture diagram  
- Supporting files  
- Scapy analysis scripts  

---

## Conclusion

This work demonstrates how throughput can be analyzed using Wireshark under controlled traffic conditions. The results show that throughput is dynamic and depends on traffic load and TCP behavior. Graph-based analysis provides a clear understanding of network performance.

---

## References

- https://www.youtube.com/watch?v=1eJHqyyjHqk  
- https://www.wireshark.org/  
- https://linux.die.net/man/8/hping3  
