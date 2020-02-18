from datetime import timedelta
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserSignup
from resources.item import Item, Items
from resources.store import Store, Stores
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'nigel'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # creates /auth
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=3600)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserSignup, '/signup')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Stores, '/stores')

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)
