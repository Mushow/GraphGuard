from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from database import init_db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Fictive user data
USER_DATA = {
    "username": "admin",
    "password": "rootroot"
}


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if data['username'] != USER_DATA['username'] or data['password'] != USER_DATA['password']:
        return jsonify({"msg": "Mauvais nom d'utilisateur ou mot de passe"}), 401

    access_token = create_access_token(identity={"username": USER_DATA['username']})
    return jsonify(access_token=access_token), 200


if __name__ == '__main__':
    init_db()
    app.run(debug=True)