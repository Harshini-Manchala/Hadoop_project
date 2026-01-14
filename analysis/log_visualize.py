import pandas as pd
import matplotlib.pyplot as plt
import os

BASE = "/home/Harshini/log_results"
PLOT_DIR = f"{BASE}/plots"

os.makedirs(PLOT_DIR, exist_ok=True)

def safe_read(path, names=None):
    try:
        return pd.read_csv(path, header=None, names=names)
    except:
        print(f"❌ ERROR reading {path}")
        return None

print("== LOADING DATA ==")

status = safe_read(f"{BASE}/status_clean.csv", ["status", "count"])
weekly = safe_read(f"{BASE}/weekly_clean.csv", ["week", "count"])
daily = safe_read(f"{BASE}/daily_clean.csv", ["day", "count"])
requests = safe_read(f"{BASE}/requests_clean.csv", ["request", "count"])
top_ips = safe_read(f"{BASE}/top_ips_clean.csv", ["ip", "count"])

# Convert numbers safely
for df in [status, weekly, daily, requests, top_ips]:
    df["count"] = pd.to_numeric(df["count"], errors="coerce")

print("== GENERATING PLOTS ==")

# ---------------- STATUS CODES ----------------
plt.figure()
status.plot(kind="bar", x="status", y="count", legend=False)
plt.title("HTTP Response Distribution")
plt.xlabel("Status Code")
plt.ylabel("Count")
plt.savefig(f"{PLOT_DIR}/status_codes.png")
plt.close()

# ---------------- WEEKLY TRAFFIC ----------------
plt.figure()
weekly.plot(x="week", y="count", legend=False)
plt.title("Weekly Traffic Trend")
plt.xlabel("Week")
plt.ylabel("Hits")
plt.xticks([])
plt.savefig(f"{PLOT_DIR}/weekly_trend.png")
plt.close()

# ---------------- DAILY TRAFFIC ----------------
plt.figure()
daily.plot(x="day", y="count", legend=False)
plt.title("Daily Traffic Trend")
plt.xlabel("Date")
plt.ylabel("Hits")
plt.xticks([])
plt.savefig(f"{PLOT_DIR}/daily_trend.png")
plt.close()

# ---------------- TOP REQUESTS ----------------
top10_req = requests.sort_values("count", ascending=False).head(10)
plt.figure()
top10_req.plot(kind="barh", x="request", y="count", legend=False)
plt.title("TOP 10 Requested URLs")
plt.savefig(f"{PLOT_DIR}/top_requests.png")
plt.close()

# ---------------- TOP IPs ----------------
top10_ip = top_ips.sort_values("count", ascending=False).head(10)
plt.figure()
top10_ip.plot(kind="barh", x="ip", y="count", legend=False)
plt.title("TOP 10 Visitors by IP")
plt.savefig(f"{PLOT_DIR}/top_ips.png")
plt.close()

print("\n🎉 DONE! All charts saved in:")
print(f"➡  {PLOT_DIR}")
