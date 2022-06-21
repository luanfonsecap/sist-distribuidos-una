import requests
r = requests.get('http://www.google.com/search',
                 params={'q': 'Protocolo HTTP'})

if (r.status_code == 200):
    f = open('google.html', "x")
    f.write(r.text)
    f.close()
else:
    print('Nao houve sucesso na requisição.')
