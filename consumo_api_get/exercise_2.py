import requests

url = 'https://viacep.com.br/ws/'
zipcode = 30140071
formato = '/json/'

zipcodes = range(zipcode, zipcode + 5)

for item in zipcodes:
    r = requests.get(url + str(item) + formato)

    if (r.status_code == 200):
        print()
        print('JSON : ', r.json())
        print()
    else:
        print('Nao houve sucesso na requisição.')
