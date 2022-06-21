
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)


# Importa classes de modelo
from app.models import estacao
db.create_all()

# Importa classes controladoras
from app.controllers.estacao_controller import EstacaoController
app.register_blueprint(EstacaoController.estacao_controller, url_prefix="/api/v1")