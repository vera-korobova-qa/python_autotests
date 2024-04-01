import requests
import pytest

URL = 'https://api.pokemonbattle.me'
HEADER = {'Content-Type': 'application/json'}

def test_get_trainers():
    responce = requests.get(url=f'{URL}/trainers', params={'level': 5}, timeout=5)
    assert responce.status_code == 200, 'Unexpected status code'

def test_get_my_trainer():
    responce = requests.get(url=f'{URL}/trainers', params={'trainer_id': 880}, timeout=5)
    assert responce.json()['trainer_name'] == 'Crane', ''
    print(f'Имя: {responce.json()["trainer_name"]}')
