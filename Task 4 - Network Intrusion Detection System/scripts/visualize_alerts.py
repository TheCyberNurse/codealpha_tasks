import json
from collections import Counter
import matplotlib.pyplot as plt

eve_file = r"C:\Suricata-Task4\log\eve.json"
output_file = r"C:\Suricata-Task4\output\alerts_by_signature.png"

alerts = []

with open(eve_file, "r", encoding="utf-8") as file:
    for line in file:
        try:
            event = json.loads(line)

            if event.get("event_type") == "alert":
                signature = event.get("alert", {}).get(
                    "signature", "Unknown Alert"
                )
                alerts.append(signature)

        except json.JSONDecodeError:
            continue

if not alerts:
    print("No Suricata alerts were found in eve.json.")
    raise SystemExit

alert_counts = Counter(alerts)

plt.figure(figsize=(10, 6))
plt.bar(alert_counts.keys(), alert_counts.values())

plt.title("Suricata Network Intrusion Alerts")
plt.xlabel("Alert Signature")
plt.ylabel("Number of Alerts")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

plt.savefig(output_file, dpi=300)
plt.close()

print(f"Visualization created successfully: {output_file}")
print(f"Total alerts analyzed: {len(alerts)}")