from serpapi import GoogleSearch

params = {
  "engine": "google_flights",
  "departure_id": "PEK",
  "arrival_id": "AUS",
  "outbound_date": "2024-02-11",
  "return_date": "2024-02-17",
  "currency": "USD",
  "hl": "en",
  "api_key": "cdfd14d194e22fc0da54f1698c9ef3bdceda237acd7460de22455ed562bd6cee"
}

search = GoogleSearch(params)
results = search.get_dict()

print(results)