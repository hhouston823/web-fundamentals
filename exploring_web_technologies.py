import requests
import json

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    return response.json()

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon["weight"]
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data = [fetch_pokemon_data(name) for name in pokemon_names]

for pokemon in pokemon_data:
    name = pokemon["name"]
    abilities = [ability["ability"]["name"] for ability in pokemon["abilities"]]
    print(f"Name: {name}, Abilities: {', '.join(abilities)}")

average_weight = calculate_average_weight(pokemon_data)
print(f"Average Weight: {average_weight}")