import requests

ROUTER_IP = "192.168.88.1"
USER = "admin"
PASSWORD = ""

url = f"http://{ROUTER_IP}/rest/ip/address"

response = requests.get(url, auth=(USER, PASSWORD))

if response.status_code == 200:
    addresses = response.json()
    for item in addresses:
        print(f"ID: {item.get('.id')} | Adresa: {item.get('address')} | Rozhranie: {item.get('interface')}")
else:
    print(f"Chyba: {response.status_code}")
    print(response.text)
