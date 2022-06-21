import sqlite3
import dao
from dao.CondTempoDAO import CondTempoDAO

class SqliteTempoDAO(CondTempoDAO):

    def adicionar(self, tempo):

        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()

        query = 'INSERT INTO cond_tempo VALUES (NULL,?,?,?,?,?,?,?)'
        registro = (tempo.cidade, tempo.tempe, tempo.umidade, tempo.descrip, tempo.vento, tempo.dia, tempo.hora)

        try:
            cursor.execute(query, registro)
            conexao.commit()
        except sqlite3.Error as err:
            raise Exception(f'Error: {err}')
        finally:
            if conexao:
                conexao.close()


    def selecionar_tempo(self):
        pass

    def excluir_tempo(self, id):
        pass

    def buscar_tempo(self):
        conexao = dao.SqliteDAOFactory.criar_conexao()
        cursor = conexao.cursor()
        query = 'SELECT * FROM cond_tempo WHERE DATE(data_hora_coleta) = DATE();'

        try:
            dados = cursor.execute(query).fetchone()

        except sqlite3.Error as e:
            raise Exception(f'Erro: {e}')
        finally:
            if conexao:
                conexao.close()