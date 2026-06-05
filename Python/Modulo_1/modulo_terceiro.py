# pip install requests

print("\nImportação e uso de um módulo de terceiros - requests")

import requests

url = "https://www.riotgames.com/pt-br"
response = requests.get(url)

print(f"\nSolicitação HTTP para {url} retornou o status {response.status_code}")