# CodeAlpha Network Intrusion Detection System

## Project Overview

This project is a network-based Intrusion Detection System (IDS) developed as part of the CodeAlpha Cyber Security Internship — Task 4.

The project uses Suricata to monitor network traffic, detect suspicious activity using a custom detection rule, generate alerts, record events in EVE JSON format, and support incident response through a Python-based response mechanism.

A Python visualization script was also used to analyze the detected alerts and generate a graphical representation of the results.

## Objectives

* Set up a network-based intrusion detection system.
* Configure rules to detect suspicious network activity.
* Monitor network traffic for potential threats.
* Generate and record security alerts.
* Implement a basic response mechanism for detected alerts.
* Visualize detected alerts for easier analysis.

## Tools and Technologies

* Suricata 8.0.7 — Network Intrusion Detection System
* Npcap — Packet capture support on Windows
* Python — Alert processing, response handling, and visualization
* Matplotlib — Alert visualization
* Windows 11
* EVE JSON — Structured security event logging

## Detection Rule

A custom Suricata rule was created to detect DNS queries for a test domain:

`codealpha-test.local`

The rule generates an alert with the signature:

`CodeAlpha Task 4 - DNS Test Alert`

The rule is located in:

`rules/local.rules`

## Network Monitoring

Suricata was configured to monitor live network traffic through the active Wi-Fi network interface using PCAP capture.

The IDS was tested by generating DNS requests for the test domain.

Although the test domain does not exist, the DNS request itself provided network traffic that could be inspected and matched by the custom Suricata rule.

## Alert Detection

The custom rule successfully generated Suricata alerts.

The detected events included information such as:

* Timestamp
* Source IP address
* Source port
* Destination IP address
* Destination port
* Network protocol
* Alert signature
* Severity
* DNS query information

The alerts were recorded in Suricata's `eve.json` log.

## Incident Response Mechanism

A Python script was created to process Suricata alert events from `eve.json`.

The script extracts important alert information and generates a response log containing:

* Alert timestamp
* Alert signature
* Severity
* Source and destination information
* Network protocol
* Recommended response action

The response mechanism is located in:

`scripts/response_handler.py`

The generated response log is stored in:

`output/incident_response.txt`

## Alert Visualization

A Python script was used to analyze the Suricata alerts and generate a graphical visualization using Matplotlib.

The visualization shows the number of alerts detected for each alert signature.

The visualization script is located in:

`scripts/visualize_alerts.py`

The generated graph is stored in:

`output/alerts_by_signature.png`

## Test Results

The custom Suricata rule successfully detected **4 DNS alert events** during testing.

The alerts were generated from network traffic captured during the IDS test.

The detected activity was recorded in EVE JSON format, processed by the Python response mechanism, and visualized in a graph.

## Project Structure

```text
Task 4 - Network Intrusion Detection System/
├── rules/
│   └── local.rules
├── scripts/
│   ├── response_handler.py
│   └── visualize_alerts.py
├── output/
│   ├── alerts_by_signature.png
│   └── incident_response.txt
└── README.md
```

## Detection and Response Workflow

```text
Network Traffic
       ↓
   Suricata IDS
       ↓
Detection Rule
       ↓
Security Alert
       ↓
   EVE JSON Log
       ↓
Python Response Handler
       ↓
Incident Response Log
```

Alert visualization workflow:

```text
EVE JSON Log
       ↓
Python Visualization Script
       ↓
Alert Visualization
```

## Limitations

This project demonstrates an Intrusion Detection System (IDS) configuration.

The current implementation detects and records suspicious activity and provides recommended response actions. It does not automatically block network traffic or act as an active IPS/firewall.

## Internship

**CodeAlpha Cyber Security Internship — Task 4**

**Project:** Network Intrusion Detection System

**Status:** Completed
