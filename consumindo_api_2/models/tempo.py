class Tempo:

    def __init__(self, id: int = -1, cidade: str = '', tempe: float = 0, data: str = '', hora: str = '',
                 descrip: str = '', turno: str = '', umidade: float = 0, vento: float = 0, nascersol: str = '',
                 porsol: str = '', condtempo: str = '', semana_min: float = 0, semana_max: float = 0):
        super().__init__()

        self.__id = id
        self.__cidade = cidade
        self.__tempe = tempe
        self.__data = data
        self.__hora = hora
        self.__descrip = descrip
        self.__turno = turno
        self.__umidade = umidade
        self.__vento = vento
        self.__nascersol = nascersol
        self.__porsol = porsol
        self.__condtempo = condtempo
        self.__semana_min = semana_min
        self.__semana_max = semana_max

        @property
        def id(self):
            return self.__id

        @id.setter
        def id(self, value):
            return  self.__id

        @property
        def cidade(self):
            return self.__cidade

        @cidade.setter
        def cidade(self, value):
            return self.__cidade

        @property
        def tempe(self):
            return self.__temp

        @tempe.setter
        def tempe(self, value):
            return self.__tempe

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            return self.__data

        @property
        def hora(self):
            return self.__hora

        @hora.setter
        def hora(self, value):
            return self.__hora

        @property
        def descrip(self):
            return self.__descrip

        @descrip.setter
        def descrip(self, value):
            return self.__descrip

        @property
        def turno(self):
            return self.__turno

        @turno.setter
        def turno(self, value):
            return self.__turno

        @property
        def umidade(self):
            return self.__umidade

        @umidade.setter
        def umidade(self, value):
            return self.__umidade

        @property
        def vento(self):
            return self.__vento

        @vento.setter
        def vento(self, value):
            return self.__vento

        @property
        def nascersol(self):
            return self.__nascersol

        @nascersol.setter
        def nascersol(self, value):
            return self.__nascersol

        @property
        def porsol(self):
            return self.__porsol

        @porsol.setter
        def porsol(self, value):
            return self.__porsol

        @property
        def condtempo(self):
            return self.__condtempo

        @condtempo.setter
        def condtempo(self, value):
            return self.__condtempo

        @property
        def semana_min(self):
            return self.__semana_min

        @semana_min.setter
        def semana_min(self, value):
            return self.__semana_min

        @property
        def semana_max(self):
            return self.__semana_max

        @semana_max.setter
        def semana_max(self, value):
            return self.__semana_max

    def imprimir(self):
        print(f'Cidade: {self.__cidade}')
        print(f'Temperatura atual: {self.__tempe}º')
        print(f'Data e Hora da consulta: {self.__data} {self.__hora}')
        print(f'Descrição do tempo atual: {self.__descrip}')
        print(f'Turno: {self.__turno}')
        print(f'Umidade: {self.__umidade}')
        print(f'Velocidade do vento: {self.__vento}')
        print(f'Nascer do sol: {self.__nascersol}')
        print(f'Pôr do sol: {self.__porsol}')
        print(f'Condição de tempo atual: {self.__condtempo}')
        print(f'Médias das temperaturas máxima e mínima da semana: ')

        print('Min: ')
        min = (round(self.__semana_min / 7, 2))
        print(min)
        print('Max: ')
        max = (round(self.__semana_max / 7, 2))
        print(max)