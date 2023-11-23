travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_visited,times_visited,cities_visited):
    new_entry = {}
    new_entry['country'] = country_visited
    new_entry['visits'] = times_visited
    new_entry['cities'] = cities_visited
    travel_log.append(new_entry)

add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)
