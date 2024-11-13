import requests
import json

headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7',
    'content-type': 'application/json',
    # 'cookie': 'wdi=2|0B0151564508C8CA|0x1.9ccfcc311ae71p+30|393d75c026b6fe3e; bse=c7ce37006ff148088edadcfd1e63340f; location=%7B%22city%22%3A+%22Vancouver%22%2C+%22state%22%3A+%22BC%22%2C+%22country%22%3A+%22CA%22%2C+%22latitude%22%3A+49.263326%2C+%22longitude%22%3A+-123.116554%2C+%22max_latitude%22%3A+49.299564%2C+%22min_latitude%22%3A+49.2270873%2C+%22max_longitude%22%3A+-123.0426747%2C+%22min_longitude%22%3A+-123.1904327%2C+%22zip%22%3A+%22%22%2C+%22address1%22%3A+%22%22%2C+%22address2%22%3A+%22%22%2C+%22address3%22%3A+null%2C+%22neighborhood%22%3A+null%2C+%22borough%22%3A+null%2C+%22provenance%22%3A+%22YELP_GEOCODING_ENGINE%22%2C+%22display%22%3A+%22Vancouver%2C+BC%22%2C+%22unformatted%22%3A+%22Vancouver%2C+BC%22%2C+%22isGoogleHood%22%3A+null%2C+%22usingDefaultZip%22%3A+null%2C+%22accuracy%22%3A+4.0%2C+%22language%22%3A+null%7D; hl=en_CA; bsi=1%7Cd1168dd7-61e6-5049-b763-760dbce8cdac%7C1731457913992%7C1731457804277%7C1%7C2436f4fe031880d8; zss=BHn4vOLFEFsvG2jUiDxqtGjOgfMzZw; recentlocations=Vancouver%2C+BC; spses.542e=*; datadome=ERrF0vLweKNM3rJxSZfme7di8JdKtqbcaVsBarUzyG71omidepLgMUgWGcqrdkITVAxm9i~BIWYk8m2iHTQslVOrJfdCq~Q56S7X3eLW3uEoU4RZFwKZiVih2IfkmhVJ; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Nov+12+2024+16%3A32%3A10+GMT-0800+(Pacific+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&consentId=consumer-xv5I4oJolKl5qOy5i75LKw&identifierType=Cookie+Unique+Id&hosts=&interactionCount=1&isAnonUser=0&landingPath=https%3A%2F%2Fwww.yelp.ca%2Fvancouver&groups=BG122%3A1%2CC0003%3A1%2CC0002%3A1%2CC0001%3A1%2CC0004%3A1; xcj=1|CBeCf_SpusqS_T1-iQn8-8AmY_Nmw77YkVaVWm7qBnA; spid.542e=844a758c-cd07-476e-ba1c-85e1d1c5c05a.1731457925.1.1731457942..d0c5eef6-d5a2-4fa1-b41a-603a559677a9..e284bc95-2f02-4fae-a4ba-6196d488996e.1731457925079.6',
    'origin': 'https://www.yelp.ca',
    'priority': 'u=1, i',
    'referer': 'https://www.yelp.ca/vancouver',
    'sec-ch-device-memory': '8',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-arch': '"arm"',
    'sec-ch-ua-full-version-list': '"Chromium";v="130.0.6723.117", "Google Chrome";v="130.0.6723.117", "Not?A_Brand";v="99.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'x-apollo-operation-name': 'GetRecentActivityFeedData,GetConsumerFooterCopyrightData',
}

json_data = [
    {
        'operationName': 'GetRecentActivityFeedData',
        'variables': {
            'resultsPerPage': 60,
            'after': None,
            'feed': 'FRIENDS',
            'nearbyFeed': True,
            'reactionsSourceFlow': 'activityFeed',
        },
        'extensions': {
            'operationType': 'query',
            'documentId': '2d23ef16b7b29bc39c2c2b51a4561136a65a9cd8c8d832e94b62856ae03778bb',
        },
    },
    {
        'operationName': 'GetConsumerFooterCopyrightData',
        'variables': {},
        'extensions': {
            'operationType': 'query',
            'documentId': '7afdec92e3e0c56c236ac65165bcf2d8c6bd183b1f232703501e65f295108b7a',
        },
    },
]

response = requests.post('https://www.yelp.ca/gql/batch', headers=headers, json=json_data)

data = response.json()

informations = data[0]['data']['nearbyActivityFeed']['edges']

parsed_data = []


for info in informations:
    place = info['node']['items'][0]
    place_info = {}

    print(place)

    place_info['name'] = info['businessPhoto']['business']['name']
    place_info['image'] = info['businessPhoto']['photoBusiness']['primaryPhoto']['photoUrl']['url1x']
    place_info['price_range'] = info['businessPhoto']['business']['priceRange']['display']
    place_info['rating'] = info['businessPhoto']['business']['rating']
    place_info['review_count'] = info['businessPhoto']['business']['reviewCount']

    parsed_data.append(place_info)

with open("yelp2.json", "w", encoding="utf-8") as file:
    file.write(json.dumps(parsed_data, indent=4))