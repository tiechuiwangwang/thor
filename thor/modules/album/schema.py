from flask_restful import fields


PHOTO = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'image_url': fields.String,
}
