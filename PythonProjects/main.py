import requests

URL = 'https://api.pokemonbattle.me'
HEADER = {'Content-Type': 'application/json', "trainer_token": "fd8e217ddea119cd450a18327a32e58a"}
body1 = {
    "name": "generate",
    "photo": "generate"
}

body2= {
    "pokemon_id": "15116",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

body3= {
    "pokemon_id": "15116"
}

responce = requests.post(url=f'{URL}/pokemons', json=body1, headers=HEADER)
print(f'Статус код: {responce.status_code}. Сообщение: {responce.json()["message"]}')

responce = requests.put(url=f'{URL}/pokemons', json=body2, headers=HEADER)
print(f'Статус код: {responce.status_code}. Сообщение: {responce.json()["message"]}')

responce = requests.post(url=f'{URL}/trainers/add_pokeball', json=body3, headers=HEADER)
print(f'Статус код: {responce.status_code}. Сообщение: {responce.json()["message"]}')
