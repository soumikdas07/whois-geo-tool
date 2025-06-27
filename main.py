import whois
import requests
import socket

def get_whois_info(domain):
    print("\n🔍 WHOIS Information:")
    try:
        w = whois.whois(domain)
        for key in ['domain_name', 'registrar', 'creation_date', 'expiration_date', 'emails']:
            print(f"{key.capitalize()}: {w.get(key)}")
    except Exception as e:
        print(f"Could not retrieve WHOIS info: {e}")

def get_ip_info(domain):
    print("\n🌍 IP Geolocation Info:")
    try:
        ip = socket.gethostbyname(domain)
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        data = response.json()
        for key in ['ip', 'city', 'region', 'country', 'org', 'loc']:
            print(f"{key.capitalize()}: {data.get(key)}")
    except Exception as e:
        print(f"Could not retrieve IP info: {e}")

def run_tool():
    target = input("Enter a domain or IP address: ").strip()
    get_whois_info(target)
    get_ip_info(target)

if __name__ == "__main__":
    run_tool()
