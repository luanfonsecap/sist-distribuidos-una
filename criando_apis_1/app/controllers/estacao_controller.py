from flask import Blueprint, make_response, jsonify, request

from app import db
from app.models.estacao import Estacao
from app.models.estacao_schema import EstacaoSchema


class EstacaoController:

    estacao_controller = Blueprint(name='estacao_controller', import_name=__name__)

    @estacao_controller.route('/estacoes', methods=['GET'])
    def index():
        lista_de_estacoes = Estacao.query.all()
        estacao_schema = EstacaoSchema(many=True)
        estacoes = estacao_schema.dump(lista_de_estacoes)

        return make_response(jsonify({
            "estacoes": estacoes
        }))

    @estacao_controller.route('/estacoes/<id_estacao>', methods=['GET'])
    def get_estacao(id_estacao):

        estacao = Estacao.query.get(id_estacao)
        estacao_schema = EstacaoSchema()
        estacoes = estacao_schema.dump(estacao)

        return make_response(jsonify({
            "estacoes": estacoes
        }))

    @estacao_controller.route('/estacoes', methods=['POST'])
    def create():
        dados = request.get_json()
        estacao_schema = EstacaoSchema()
        estacao = estacao_schema.load(dados)

        print(estacao)

        resultado = estacao_schema.dump(estacao.create())

        return make_response(jsonify({
            "estacoes": resultado
        }), 201)

    @estacao_controller.route('/estacoes/<id_estacao>', methods=['DELETE'])
    def delete(id_estacao):
        estacao = Estacao.query.get(id_estacao)
        db.session.delete(estacao)
        db.session.commit()
        return make_response(jsonify({}), 204)

    @estacao_controller.route('/estacoes/<id_estacao>', methods=['PUT'])
    def update(id_estacao):

        estacao = Estacao.query.get(id_estacao)
        dados = request.get_json().get('estacoes')

        estacao_schema = EstacaoSchema()

        if dados.get('nome_estacao'):
            estacao.nome_estacao = dados['nome_estacao']

        if dados.get('cod_regiao'):
            estacao.cod_regiao = dados['cod_regiao']

        if dados.get('uf'):
            estacao.uf = dados['uf']

        if dados.get('latitude'):
            estacao.latitude = dados['latitude']

        if dados.get('longitude'):
            estacao.longitude = dados['longitude']

        if dados.get('altitude'):
            estacao.altitude = dados['altitude']

        if dados.get('datafundacao'):
            estacao.datafundacao = dados['datafundacao']

        db.session.add(estacao)
        db.session.commit()

        estacao_atualizado = estacao_schema.dump(estacao)

        return make_response(jsonify({
            "estacoes": estacao_atualizado
        }), 200)
