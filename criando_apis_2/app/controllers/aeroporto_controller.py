from flask import Blueprint, make_response, jsonify, request

from app import db
from app.models.aeroporto import Aeroporto
from app.models.aeroporto_schema import AeroportoSchema


class AeroportoController:

    aeroporto_controller = Blueprint(name='aeroporto_controller', import_name=__name__)

    @aeroporto_controller.route('/aeroportos', methods=['GET'])
    def index():
        lista_de_aeroportos = Aeroporto.query.all()
        aeroporto_schema = AeroportoSchema(many=True)
        aeroportos = aeroporto_schema.dump(lista_de_aeroportos)

        return make_response(jsonify({
            "aeroportos": aeroportos
        }))

    @aeroporto_controller.route('/aeroportos/<id_aeroporto>', methods=['GET'])
    def get_aeroporto(id_aeroporto):

        aeroporto = Aeroporto.query.get(id_aeroporto)
        aeroporto_schema = AeroportoSchema()
        aeroportos = aeroporto_schema.dump(aeroporto)

        return make_response(jsonify({
            "aeroportos": aeroportos
        }))

    @aeroporto_controller.route('/aeroportos', methods=['POST'])
    def create():
        dados = request.get_json()
        aeroporto_schema = AeroportoSchema()
        aeroporto = aeroporto_schema.load(dados)

        print(aeroporto)

        resultado = aeroporto_schema.dump(aeroporto.create())

        return make_response(jsonify({
            "aeroporto": resultado
        }), 201)

    @aeroporto_controller.route('/aeroportos/<id_aeroporto>', methods=['DELETE'])
    def delete(id_aeroporto):
        aeroporto = Aeroporto.query.get(id_aeroporto)
        db.session.delete(aeroporto)
        db.session.commit()
        return make_response(jsonify({}), 204)

    @aeroporto_controller.route('/aeroportos/<id_aeroporto>', methods=['PUT'])
    def update(id_aeroporto):

        aeroporto = Aeroporto.query.get(id_aeroporto)
        dados = request.get_json().get('aeroportos')

        aeroporto_schema = AeroportoSchema()

        if dados.get('nome_aeroporto'):
            aeroporto.nome_aeroporto = dados['nome_aeroporto']

        if dados.get('codigo_iata'):
            aeroporto.codigo_iata = dados['codigo_iata']

        if dados.get('cidade'):
            aeroporto.cidade = dados['cidade']

        if dados.get('codigo_pais_iso'):
            aeroporto.codigo_pais_iso = dados['codigo_pais_iso']

        if dados.get('latitude'):
            aeroporto.latitude = dados['latitude']

        if dados.get('longitude'):
            aeroporto.longitude = dados['longitude']

        if dados.get('altitude'):
            aeroporto.altitude = dados['altitude']

        db.session.add(aeroporto)
        db.session.commit()

        aeroporto_atualizado = aeroporto_schema.dump(aeroporto)

        return make_response(jsonify({
            "aeroportos": aeroporto_atualizado
        }), 200)
