import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("top_ips_final.csv", names=["ip", "count"])

# Convert count to numeric
df["count"] = pd.to_numeric(df["count"], errors="coerce")

# Drop missing
df = df.dropna()

# ML Model: Isolation Forest
model = IsolationForest(contamination=0.03, random_state=42)
df["anomaly"] = model.fit_predict(df[["count"]])
df["score"] = model.decision_function(df[["count"]])

# Save anomalies
df[df["anomaly"] == -1].to_csv("ip_anomalies.csv", index=False)

print("✔ Anomaly detection complete. Saved as ip_anomalies.csv")

# Plot
plt.figure(figsize=(10,6))
plt.scatter(df.index, df["count"], c=df["anomaly"], cmap="coolwarm")
plt.title("Anomaly Detection on IP Counts")
plt.xlabel("IP Record Index")
plt.ylabel("Request Count")

# SAVE PLOT
plt.savefig("anomaly_plot.png")
print("✔ Saved anomaly plot as anomaly_plot.png")

