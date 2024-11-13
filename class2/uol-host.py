import requests
import json

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://uolhost.uol.com.br',
    'priority': 'u=1, i',
    'referer': 'https://uolhost.uol.com.br/',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

domain = input("add a domain name ")

json_data = {
    'campaign': 'KsW2VVueZgLMK96ewVO1eq1GogfqMgGPCXZJIxyM',
    'domain': domain + '.com.br',
    'filters': {
        'tlds': [
            '.com.br',
            '.com',
            '.online',
            '.store',
            '.site',
            '.me',
            '.website',
            '.tech',
            '.space',
            '.net',
        ],
    },
}

response = requests.post(
    'https://rest.dominios.uolhost.uol.com.br/v1/search/public/domain-with-suggestions',
    headers=headers,
    json=json_data,
)

data = response.json()

with open("uol-host.json", "w", encoding="utf-8") as file:
  file.write(json.dumps(data))