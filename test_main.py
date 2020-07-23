from main import get_temperature
import requests


class MockResponse:

    def __init__(self, resposta):
        self.resposta = resposta

    def json(self):
        return self.resposta


def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -14.235004
    lng = -51.92528
    resposta_mock = {"currently": {"temperature": 62}}

    def mock_get(*args, **kwargs):
        return MockResponse(resposta_mock)
    monkeypatch.setattr(requests, "get", mock_get)
    resultado = get_temperature(lat, lng)
    assert resultado == 16


def test_status_code_request():
    lat = -14.235004
    lng = -51.92528
    key = 'e1ee55658d4a2b28c4841e373c3b3d87'
    url = 'https://api.darksky.net/forecast/{}/{},{}'.format(key, lat, lng)
    response = requests.get(url)
    # Verifica o status da requisição, se ela ocorreu com sucesso.
    resposta = response.status_code
    assert resposta == 200
