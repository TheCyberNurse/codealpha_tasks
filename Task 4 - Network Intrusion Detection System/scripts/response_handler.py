import json
from datetime import datetime

eve_file = r"C:\Suricata-Task4\log\eve.json"
response_file = r"C:\Suricata-Task4\output\incident_response.txt"

responses = []

with open(eve_file, "r", encoding="utf-8") as file:
    for line in file:
        try:
            event = json.loads(line)

            if event.get("event_type") != "alert":
                continue

            alert = event.get("alert", {})

            timestamp = event.get("timestamp", "Unknown")
            signature = alert.get("signature", "Unknown Alert")
            severity = alert.get("severity", "Unknown")
            src_ip = event.get("src_ip", "Unknown")
            src_port = event.get("src_port", "Unknown")
            dest_ip = event.get("dest_ip", "Unknown")
            dest_port = event.get("dest_port", "Unknown")
            protocol = event.get("proto", "Unknown")

            if severity == 1:
                recommended_action = "Immediate investigation and containment recommended."
            elif severity == 2:
                recommended_action = "Investigate the source and review related network activity."
            else:
                recommended_action = "Monitor the activity and investigate the alert details."

            response_entry = f"""
Timestamp: {timestamp}
Alert: {signature}
Severity: {severity}
Source: {src_ip}:{src_port}
Destination: {dest_ip}:{dest_port}
Protocol: {protocol}
Recommended Response: {recommended_action}
----------------------------------------
"""

            responses.append(response_entry)

        except json.JSONDecodeError:
            continue

if not responses:
    print("No Suricata alerts were found.")
    raise SystemExit

with open(response_file, "w", encoding="utf-8") as file:
    file.write("SURICATA INCIDENT RESPONSE LOG\n")
    file.write("=" * 40 + "\n")

    for response in responses:
        file.write(response)

print("Incident response log created successfully.")
print(f"Alerts processed: {len(responses)}")
print(f"Response log: {response_file}")