import sqlite3

from dao.dao_factory import DAOFactory
from dao.sqlite_cond_tempo_dao import SqliteTempoDAO


class SqliteDAOFactory(DAOFactory):

    url_DB = 'db/condicao_tempo.db'

    @staticmethod
    def criar_conexao():

        conexao = None

        try:
            conexao = sqlite3.connect(SqliteDAOFactory.url_DB)

        except sqlite3.Error as err:
            raise Exception(err)

        return conexao

    def dao_factory(self) -> DAOFactory:
        return SqliteDAOFactory()

    @property
    def tempo_dao(self):
        return SqliteTempoDAO()
