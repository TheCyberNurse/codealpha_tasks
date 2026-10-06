from scapy.all import sniff, IP, TCP, UDP, Raw

print("Network Sniffer Started")

packets = sniff(count=10)

print("\nCaptured Packets:")
print(packets.summary())

for packet in packets:
    print("\n" + "=" * 60)
    print(packet.summary())

    if packet.haslayer(IP):
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        print("Source IP:", source_ip)
        print("Destination IP:", destination_ip)

        if packet.haslayer(TCP):
            print("Protocol: TCP")
            print("Source port:", packet[TCP].sport)
            print("Destination port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Protocol: UDP")
            print("Source port:", packet[UDP].sport)
            print("Destination port:", packet[UDP].dport)

        else:
            print("Protocol number:", packet[IP].proto)
            print("Ports: Not applicable")

        if packet.haslayer(Raw):
            payload = bytes(packet[Raw].load)

            print("Payload length:", len(payload), "bytes")
            print("Payload preview:", payload[:100])

        else:
            print("Payload: None")

    else:
        print("This packet does not contain an IPv4 layer.")

print("\nNetwork Sniffer Finished")
