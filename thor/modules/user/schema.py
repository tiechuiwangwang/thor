from flask_restful import fields


USER = {
    'id': fields.Integer,
    'username': fields.String,
    'nickname': fields.String,
    'avatar': fields.String,
}
