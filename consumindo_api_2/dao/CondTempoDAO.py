from abc import abstractmethod, ABC


class CondTempoDAO(ABC):

    @abstractmethod
    def adicionar_tempo(self, tempo):
        pass

    @abstractmethod
    def selecionar_tempo(self):
        pass

    @abstractmethod
    def excluir_tempo(self, id):
        pass

    @abstractmethod
    def buscar_tempo(self):
        pass
