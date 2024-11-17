from flask import g, current_app, Response     
from flask import Flask, render_template
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.asiamodels import AsiaUserAM, AsiaUserNZ, AsiaGenericProducts, AsiaRegionalProducts, AsiaUserAMmembership, AsiaUserNZmembership
import flask_restful as restful
from flask import jsonify
import json

#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
#blueprint = Blueprint('carsdb2',__name__)

class AsiaUserAMList(restful.Resource):
    
    def get(self):
        q = AsiaUserAM.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        #return render_template('users_am.html', q=q)
        
        # TODO: fix this properly
        html_content = render_template('users.html', q=q, database="Asia", table= "useram")
        return Response(html_content, mimetype='text/html')

class AsiaUserNZList(restful.Resource):
    
    def get(self):
        q = AsiaUserNZ.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('users.html', q=q, database="Asia", table= "usernz")
        return Response(html_content, mimetype='text/html')

class AsiaGenericProductsList(restful.Resource):
    
    def get(self):
        q = AsiaGenericProducts.query.all()  
        html_content = render_template('products.html', q=q, database="Asia", table= "genericproducts")
        return Response(html_content, mimetype='text/html')


class AsiaRegionalProductsList(restful.Resource):
    
    def get(self):
        q = AsiaRegionalProducts.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('products.html', q=q, database="Asia", table= "regionalproducts")
        return Response(html_content, mimetype='text/html')


class AsiaUserAMmembershipList(restful.Resource):
    
    def get(self):
        q = AsiaUserAMmembership.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('membership.html', q=q, database="Asia", table= "asiauserammembership")
        return Response(html_content, mimetype='text/html')


class AsiaUserNZmembershipList(restful.Resource):
    
    def get(self):
        q = AsiaUserNZmembership.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('membership.html', q=q, database="Asia", table= "asiausernzmembership")
        return Response(html_content, mimetype='text/html')

