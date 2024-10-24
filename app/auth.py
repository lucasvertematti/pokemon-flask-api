from flask import Blueprint, request, jsonify
import jwt
from datetime import datetime, timedelta
from .config import Config

auth = Blueprint('auth', __name__)

# Simples autenticação via POST (poderia ser substituída por algo mais robusto)
@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] == 'admin' and data['password'] == 'password':  # Substituir com lógica real
        token = jwt.encode({
            'user': data['username'],
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, Config.SECRET_KEY)
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 403

        return f(*args, **kwargs)
    return decorator
