from sqlalchemy import Column, BigInteger, String, Integer, Numeric, DateTime, CheckConstraint
from sqlalchemy.sql.functions import current_timestamp

from app import db


class Aeroporto(db.Model):

    __tablename__ = 'Aeroporto'

    id_aeroporto = Column(BigInteger, primary_key=True)
    nome_aeroporto = Column(String(128), nullable=False)
    codigo_iata = Column(String(128), nullable=False)
    cidade = Column(String(128), nullable=False)
    codigo_pais_iso = Column(String(128), nullable=False)
    latitude = Column(Numeric(10, 2), nullable=False, server_default="0.0")
    longitude = Column(Numeric(10, 2), nullable=False, server_default="0.0")
    altitude = Column(Numeric(10, 2), nullable=False, server_default="0.0")

    criado_em = Column(DateTime, server_default=current_timestamp())
    modificado_em = Column(
        DateTime,
        server_default=current_timestamp(),
        onupdate=current_timestamp())

    def __init__(self, nome_aeroporto: str = "", codigo_iata: str = "",cidade: str = "",codigo_pais_iso: str = "", latitude: float = 0.0, longitude: float = 0.0, altitude: float = 0.0) -> None:
        self.nome_aeroporto = nome_aeroporto
        self.codigo_iata = codigo_iata
        self.cidade = cidade
        self.codigo_pais_iso = codigo_pais_iso
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude


    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f'<Aeroporto: {self.nome_aeroporto}>'
