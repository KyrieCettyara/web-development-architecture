from sqlalchemy.exc import IntegrityError
from flask import request, jsonify, make_response
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, create_refresh_token, jwt_required, get_jwt, get_jwt_identity
from app.extensions import db, jwt
from app.auth import authBp
from app.models.user import Users
from app.models.blacklist_token import BlacklistToken

from flask_login import login_user, current_user, logout_user

@authBp.route("/register", methods=['POST'], strict_slashes =False)
def registration():
    data = request.get_json()
    print(data)
    username = data.get('username', None)
    password = generate_password_hash(data.get('password', None))
    email = data.get('email', None)
    role = data.get('role', "user")
    error = None

    if not username or not password or not email:
        return jsonify({"message": "Pastikan username, email, dan password tidak kosong."}), 400
    
    try:
        db.session.add(Users(username=username,
                                password=password,
                                email=email, role=role))
        db.session.commit()
    except IntegrityError:
        return jsonify({
            "error": "User sudah terdaftar sebelumnya",}), 400       


    response = make_response(jsonify({
        "success": True,
        "message":"Berhasil Mendaftarkan User",
        }), 200)

    return response

@authBp.route("/login", methods=['POST'], strict_slashes = False)
def login():
    # get data from request json
    data = request.get_json()
    
    # get username password from json
    username = data.get('username', None)
    password = data.get('password', None)


    error = None
    user = db.session.execute(db.select(Users).filter_by(username=username)).scalar_one()
    print([user.id, user.username,user.email, user.role ])

    if not user:
        error = "username tidak ditemukan"
        return jsonify({"error": error}), 422
    
    if not check_password_hash(user.password, password):
        error = "Password yang dimasukkan salah"
        return jsonify({"error": error}), 422


    login_user(user, remember=True)
    print(current_user)

    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)   

    response = make_response(jsonify({
        "success": True,
        "message":"Berhasil Login",
        "access_token" : access_token,
        "refresh_token": refresh_token }), 200)
    
    return response

@authBp.route('/refresh', methods=['POST'], strict_slashes = False)
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = {
        'access_token': create_access_token(identity=current_user)
    }
    return jsonify(access_token), 200

@authBp.route("/logout", methods=['POST'], strict_slashes = False)
@jwt_required(locations=["headers"])
def logout():
    logout_user()
    raw_jwt = get_jwt()

    jti = raw_jwt.get('jti')
    token = BlacklistToken(jti = jti)
    
    db.session.add(token)
    db.session.commit()


    response = make_response(jsonify(
        {
        "message":"Berhasil Logout",
        "success": True}), 200)
    return response

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token_in_redis = BlacklistToken.query.filter_by(jti=jti).first()
    return token_in_redis is not None