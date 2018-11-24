from flask import Blueprint, request
from backend.models import User
from backend import db, bcrypt
import json
from datetime import datetime, timedelta
from sqlalchemy import and_, or_

users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    request_json = request.get_json()
    email = request_json['email']
    password = request_json['password']
    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        final_dict = {
            'id': user.id,
            'auth_token': user.get_auth_token(),
            'name': user.name,
            'email': user.email,
            'status': 1
        }
        return json.dumps(final_dict)
    else:
        final_dict = {
            'status': 0,
            'error': "The provided combination of email and password is incorrect."
        }
        return json.dumps(final_dict)


@users.route('/register', methods=['GET', 'POST'])
def normal_register():
    request_json = request.get_json()
    if User.query.filter_by(email=request_json['email']).first():
        return json.dumps({'status': 0, 'output': User.query.filter_by(email=request_json['email']).first().email,
                          'error': "User Already Exists"})
    email = request_json['email']
    hashed_pwd = bcrypt.generate_password_hash(request_json['password']).decode('utf-8')
    name = request_json['name']
    # noinspection PyArgumentList
    user = User(email=email, password=hashed_pwd, name=name)
    db.session.add(user)
    db.session.commit()
    return json.dumps({'id': user.id, 'status': 1})
