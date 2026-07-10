from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database.mongo import users

import bcrypt

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["POST"])
def signup():

    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:

        return jsonify({
            "message": "All fields are required"
        }), 400

    existing_user = users.find_one({
        "email": email
    })

    if existing_user:

        return jsonify({
            "message": "Email already exists"
        }), 400

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    users.insert_one({

        "name": name,

        "email": email,

        "password": hashed_password

    })

    return jsonify({

        "message": "User created successfully"

    }), 201


@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = users.find_one({

        "email": email

    })

    if not user:

        return jsonify({

            "message": "Invalid email or password"

        }), 401

    valid = bcrypt.checkpw(

        password.encode(),

        user["password"].encode()

    )

    if not valid:

        return jsonify({

            "message": "Invalid email or password"

        }), 401

    access_token = create_access_token(

        identity=str(user["_id"])

    )

    return jsonify({

        "message": "Login successful",

        "token": access_token,

        "name": user["name"]

    })
