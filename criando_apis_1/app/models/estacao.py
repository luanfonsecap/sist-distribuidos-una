from sqlalchemy import Column, BigInteger, String, Integer, Numeric, DateTime, CheckConstraint, Date
from sqlalchemy.sql.functions import current_timestamp

from app import db


class Estacao(db.Model):

    __tablename__ = 'Estacao'

    id_estacao = Column(BigInteger, primary_key=True)
    nome_estacao = Column(String(128), nullable=False)
    cod_regiao = Column(String(128), nullable=False)
    uf = Column(String(128), nullable=False)
    codigo_wmo = Column(String(128), nullable=False)
    latitude = Column(Numeric, nullable=False, server_default="0")
    longitude = Column(Numeric, nullable=False, server_default="0")
    altitude = Column(Numeric, nullable=False, server_default="0")
    datafundacao = Column(DateTime, nullable=False)


    criado_em = Column(DateTime, server_default=current_timestamp())
    modificado_em = Column(
        DateTime,
        server_default=current_timestamp(),
        onupdate=current_timestamp())

    def __init__(self, nome_estacao: str = "", cod_regiao: str = "", uf: str = "", codigo_wmo: str = "", latitude: float = 0.0, longitude: float = 0.0, altitude: float = 0.0, datafundacao: str = "") -> None:
        self.nome_estacao = nome_estacao
        self.cod_regiao = cod_regiao
        self.uf = uf
        self.codigo_wmo = codigo_wmo
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.datafundacao = datafundacao


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Estacao: {self.nome_estacao}>'
