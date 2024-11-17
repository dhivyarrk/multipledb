from flask import g, current_app, Response     
from flask import Flask, render_template
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.europemodels import EuropeUserAM, EuropeUserNZ, EuropeGenericProducts, EuropeRegionalProducts, EuropeUserAMmembership, EuropeUserNZmembership, EuropeMetadata_Europe
import flask_restful as restful
from flask import jsonify
import json

#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
#blueprint = Blueprint('carsdb2',__name__)

class EuropeUserAMList(restful.Resource):
    
    def get(self):
        q = EuropeUserAM.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        #return render_template('users_am.html', q=q)
        
        # TODO: fix this properly
        html_content = render_template('users.html', q=q, database="Europe", table= "useram")
        return Response(html_content, mimetype='text/html')

class EuropeUserNZList(restful.Resource):
    
    def get(self):
        q = EuropeUserNZ.query.all()  
        #import jsonpickles
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('users.html', q=q, database="Europe", table= "usernz")
        return Response(html_content, mimetype='text/html')

class EuropeGenericProductsList(restful.Resource):
    
    def get(self):
        q = EuropeGenericProducts.query.all()  
        html_content = render_template('products.html', q=q, database="Europe", table= "genericproducts")
        return Response(html_content, mimetype='text/html')


class EuropeRegionalProductsList(restful.Resource):
    
    def get(self):
        q = EuropeRegionalProducts.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('products.html', q=q, database="Europe", table= "regionalproducts")
        return Response(html_content, mimetype='text/html')


class EuropeUserAMmembershipList(restful.Resource):
    
    def get(self):
        q = EuropeUserAMmembership.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('membership.html', q=q, database="Europe", table= "europeuserammembership")
        return Response(html_content, mimetype='text/html')


class EuropeUserNZmembershipList(restful.Resource):
    
    def get(self):
        q = EuropeUserNZmembership.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('membership.html', q=q, database="Europe", table= "europeusernzmembership")
        return Response(html_content, mimetype='text/html')


class EuropeMetadata_EuropeList(restful.Resource):
    
    def get(self):
        q = EuropeMetadata_Europe.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('metadata.html', q=q, database="Europe", table= "europemetadata")
        return Response(html_content, mimetype='text/html')
