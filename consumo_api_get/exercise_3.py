import requests

url = 'https://viacep.com.br/ws/'
address = 'MG/Belo Horizonte/Rua dos Aimores'
formato = '/json/'

r = requests.get(url + address + formato)

if (r.status_code == 200):
    print()
    print('JSON : ', r.json())
    print()
else:
    print('Nao houve sucesso na requisição.')
