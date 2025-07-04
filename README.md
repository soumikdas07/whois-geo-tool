# 🌐 WHOIS & IP Geolocation CLI Tool

A Python CLI tool to gather domain/IP ownership and location data. Useful for cybersecurity recon, OSINT tasks, or learning how domain registration and IP mapping works.

---

## ⚙️ Features

- 🔍 WHOIS lookup (domain name, registrar, emails, creation & expiry dates)
- 🌍 IP Geolocation lookup (city, region, country, org, coordinates)
- Supports both domain names and raw IPs
- Clean, readable CLI output
- Uses free and open web APIs

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/soumikdas07/whois-geo-tool.git
cd whois-geo-tool
```

### 2. Install Dependencies

```bash
pip install python-whois requests
```

### 3. Run the Script

```bash
python main.py
```

### 4. Sample Output

```bash
Enter a domain or IP address: google.com

🔍 WHOIS Information:
Domain_name: GOOGLE.COM
Registrar: MarkMonitor Inc.
Creation_date: 1997-09-15 04:00:00
Expiration_date: 2028-09-14 04:00:00
Emails: dns-admin@google.com

🌍 IP Geolocation Info:
Ip: 142.250.195.14
City: Mountain View
Region: California
Country: US
Org: AS15169 Google LLC
Loc: 37.4220,-122.0841
```
