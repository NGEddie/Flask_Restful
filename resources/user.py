import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


class UserSignup(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', required=True,
                        help="Username is required", type=str)
    parser.add_argument('password',
                        required=True,
                        help="Passowrd is required",
                        type=str)

    def post(self):
        data = UserSignup.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {
                'status': 'fail',
                'message': f"user: \'{data['username']}\' already exists"
            }, 400

        user = UserModel(**data)
        user.save_to_db()

        return {
            'status': 'success',
            'message': f"user: \'{data['username']}\' created successfully"
        }, 201
