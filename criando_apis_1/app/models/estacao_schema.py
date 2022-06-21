from app import ma, db
from app.models.estacao import Estacao


class EstacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Estacao
        sqla_session = db.session
        load_instance = True

    id_estacao = ma.auto_field()
    nome_estacao = ma.auto_field()
    cod_regiao = ma.auto_field()
    uf = ma.auto_field()
    codigo_wmo = ma.auto_field()
    latitude = ma.auto_field()
    longitude = ma.auto_field()
    altitude = ma.auto_field()
    datafundacao = ma.auto_field()

