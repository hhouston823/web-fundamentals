import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    # process each planet info
    heaviest_planet = None
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']
            orbit_period = planet['orbitalPeriod']

            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

            if heaviest_planet is None or mass > heaviest_planet['mass']:
                heaviest_planet = {'name': name, 'mass': mass}

    print(f"The heaviest planet in the solar system is {heaviest_planet['name']} with a mass of {heaviest_planet['mass']}")

fetch_planet_data()