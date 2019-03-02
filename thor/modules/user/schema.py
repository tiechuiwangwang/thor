from flask_restful import fields


USER_FIELDS = {
    'id': fields.Integer,
    'username': fields.String,
    'nickname': fields.String,
    'avatar': fields.String,
}
