import requests

def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/breweries?by_state={state}"
    response = requests.get(url)
    if response.status_code == 200:
        breweries = response.json()
        return breweries
    else:
        print(f"Failed to fetch data for {state}. Status code: {response.status_code}")
        return []

def count_breweries_by_state(state):
    breweries = get_breweries_by_state(state)
    if breweries:
        return len(breweries)
    else:
        return 0

def count_brewery_types_by_city(state):
    breweries = get_breweries_by_state(state)
    if breweries:
        city_types_count = {}
        for brewery in breweries:
            city = brewery['city']
            brewery_type = brewery['brewery_type']
            if city in city_types_count:
                if brewery_type not in city_types_count[city]:
                    city_types_count[city].append(brewery_type)
            else:
                city_types_count[city] = [brewery_type]
        return city_types_count
    else:
        return {}

def count_breweries_with_website(state):
    breweries = get_breweries_by_state(state)
    if breweries:
        with_website = [brewery for brewery in breweries if brewery.get('website_url')]
        return len(with_website)
    else:
        return 0

def main():
    states = ['Alaska', 'Maine', 'New York']
    for state in states:
        print(f"\nBreweries in {state}:")
        breweries = get_breweries_by_state(state)
        if breweries:
            for brewery in breweries:
                print(brewery['name'])
            print(f"Total Breweries in {state}: {count_breweries_by_state(state)}")
            print(f"Brewery types count by city:")
            city_types_count = count_brewery_types_by_city(state)
            for city, types_count in city_types_count.items():
                print(f"{city}: {len(types_count)}")
            print(f"Number of Breweries with a website in {state}: {count_breweries_with_website(state)}")
        else:
            print("No breweries found.")

if __name__ == "__main__":
    main()
