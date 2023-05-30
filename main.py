# import libraries
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from parsers import *

# initialise flask app
app = Flask(__name__)

# initialise RESTful API
api = Api(app)

# configure SQLAlchemy database to create a db in the local directory
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# create db variable linked to the current app
db = SQLAlchemy(app)


# create antibody model class for the db, including all attributes that can be processed using CRUD
class AntibodyModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marker = db.Column(db.String, nullable=False)
    fluorophore = db.Column(db.String, nullable=False)
    supplier = db.Column(db.String, nullable=False)
    code = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer)
    date = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"ID: {self.id},\n Marker: {self.marker},\n Fluorophore: {self.fluorophore},\n Supplier: {self.supplier},\n Product Code: {self.code},\n Price: {self.price},\n Order Date: {self.date}"


# create database table, should only be run once to initialise then commented out
# db.create_all()

# define resource_fields that will be used by marshal_with() to format our response before returning
resource_fields = {
    "id": fields.Integer,
    "marker": fields.String,
    "fluorophore": fields.String,
    "supplier": fields.String,
    "code": fields.String,
    "price": fields.Integer,
    "date": fields.String,
}


# create Antibody class, inheriting Resource from flask_restful which contains methods for each HTTP method
# within the class I have defined my own functions to ovewrite the default
class Antibody(Resource):
    # get function to read
    @marshal_with(resource_fields)
    def get(self, antibody_id):
        result = AntibodyModel.query.filter_by(id=antibody_id).first()
        if not result:
            abort(404, message="Antibody not found")
        return result, 200

    # post function to add new entries to the db
    @marshal_with(resource_fields)
    def post(self, antibody_id):
        args = post_parser.parse_args()
        result = AntibodyModel.query.filter_by(id=antibody_id).first()
        if result:
            abort(409, message="Antibody already exists")
        antibody = AntibodyModel(
            id=antibody_id,
            marker=args["marker"],
            fluorophore=args["fluorophore"],
            supplier=args["supplier"],
            code=args["code"],
            price=args["price"],
            date=args["date"],
        )
        db.session.add(antibody)
        db.session.commit()
        return result, 201

    # put function to completely overwrite db entries
    @marshal_with(resource_fields)
    def put(self, antibody_id):
        args = put_parser.parse_args()
        result = AntibodyModel.query.filter_by(id=antibody_id).first()
        if not result:
            abort(404, message="Antibody not found, cannot replace, please try post")
        (
            result.marker,
            result.fluorophore,
            result.supplier,
            result.code,
            result.price,
            result.date,
        ) = (
            args["marker"],
            args["fluorophore"],
            args["supplier"],
            args["code"],
            args["price"],
            args["date"],
        )
        db.session.commit()
        return result, 204

    # patch function to partially overwrite db entries
    @marshal_with(resource_fields)
    def patch(self, antibody_id):
        args = patch_parser.parse_args()
        result = AntibodyModel.query.filter_by(id=antibody_id).first()
        if not result:
            abort(404, message="Antibody not found, cannot replace, please try post")
        if args["marker"]:
            result.marker = args["marker"]
        if args["fluorophore"]:
            result.fluorophore = args["fluorophore"]
        if args["supplier"]:
            result.supplier = args["supplier"]
        if args["code"]:
            result.code = args["code"]
        if args["price"]:
            result.price = args["price"]
        if args["date"]:
            result.date = args["date"]
        db.session.commit()
        return result, 204

    # delete function to delete db entries
    def delete(self, antibody_id):
        result = AntibodyModel.query.filter_by(id=antibody_id).first()
        if not result:
            abort(404, message="Antibody does not exist")
        # result.delete()
        # AntibodyModel.query.filterby(id=antibody_id).first().delete()
        db.session.delete(result)
        db.session.commit()
        return "", 204


# adds a resource to the API, here I've included our resource Antibody, and the url that would be generated for each data entry
api.add_resource(Antibody, "/antibody/<int:antibody_id>")

# run our app in debug mode to see updates in real time
if __name__ == "__main__":
    app.run(debug=True)
