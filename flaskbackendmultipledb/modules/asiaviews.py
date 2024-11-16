from flask import g, current_app
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.asiamodels import AsiaUserAM
import flask_restful as restful
from flask import jsonify
import json

#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
#blueprint = Blueprint('carsdb2',__name__)

class AsiaUserAMList(restful.Resource):
    
    def get(self):
        q = AsiaUserAM.query.all()  
        import jsonpickle
        j = jsonpickle.encode(q)
        return j