import requests as requests
from dao.sqlite_dao_factory import SqliteDAOFactory
from models.tempo import Tempo
import config


condTempoDAO = None
tempo_hoje = None


def tempo(resposta) -> Tempo:

    if resposta.status_code == 200:
        json = resposta.json()
        dados = json['results']

        cidade = (dados['city'])
        tempe = (dados['temp'])
        data = (dados['date'])
        hora = (dados['time'])
        descrip = (dados['description'])
        turno = (dados['currently'])
        umidade = (dados['humidity'])
        vento = (dados['wind_speedy'])
        nascersol = (dados['sunrise'])
        porsol = (dados['sunset'])
        condtempo = (dados['condition_slug'])

        semana_min = 0
        semana_max = 0
        for dia in range(1, 8):
            semana_min += (dados['forecast'][dia]['min'])
            semana_max += (dados['forecast'][dia]['max'])

        return Tempo(cidade=cidade, tempe=tempe, data=data, hora=hora, descrip=descrip, turno=turno,
                     umidade=umidade, vento=vento, nascersol=nascersol, porsol=porsol, condtempo=condtempo, semana_min=semana_min, semana_max=semana_max).imprimir()


def carregar_tempo_hoje() -> Tempo:

    registro_tempo_hoje = condTempoDAO.buscar_tempo()

    if registro_tempo_hoje is None:
        tempos = tempo()
        salvar_tempo(tempos)
        return tempos

    else:
        registro_tempo_hoje = condTempoDAO.buscar_tempo_hoje()
        return Tempo(registro_tempo_hoje[0], registro_tempo_hoje[1], registro_tempo_hoje[2], registro_tempo_hoje[3])


def salvar_tempo(tempo) -> None:
    condTempoDAO.adicionar(tempo)


if __name__ == '__main__':
    cidade_estado = input("Digite a cidade e o estado")
    print()
    url =f'https://api.hgbrasil.com/weather'.format(f'?key={config.api_key}&city_name={cidade_estado}')    
    resposta = requests.get(url)
    tempo(resposta)
    sqliteFactory = SqliteDAOFactory()
    tempo_hoje = carregar_tempo_hoje()
    salvar_tempo(tempo)
