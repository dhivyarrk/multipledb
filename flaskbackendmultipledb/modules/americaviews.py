from flask import g, current_app, Response     
from flask import Flask, render_template
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.americamodels import AmericaUserAM, AmericaUserNZ, AmericaGenericProducts, AmericaRegionalProducts, AmericaUserAMmembership, AmericaUserNZmembership, AmericaMetadata_America
import flask_restful as restful
from flask import jsonify
import json

#blueprint = Blueprint('db1', __name__, url_prefix='/db1')
#blueprint = Blueprint('carsdb2',__name__)

class AmericaUserAMList(restful.Resource):
    
    def get(self):
        q = AmericaUserAM.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        #return render_template('users_am.html', q=q)
        
        # TODO: fix this properly
        html_content = render_template('users.html', q=q, database="America", table= "useram")
        return Response(html_content, mimetype='text/html')

class AmericaUserNZList(restful.Resource):
    
    def get(self):
        q = AmericaUserNZ.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        html_content = render_template('users.html', q=q, database="America", table= "usernz")
        return Response(html_content, mimetype='text/html')

class AmericaGenericProductsList(restful.Resource):
    
    def get(self):
        q = AmericaGenericProducts.query.all()  
        return render_template('generic_products.html', q=q)


class AmericaRegionalProductsList(restful.Resource):
    
    def get(self):
        q = AmericaRegionalProducts.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        return render_template('regional_products.html', q=q)


class AmericaUserAMmembershipList(restful.Resource):
    
    def get(self):
        q = AmericaUserAMmembership.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        return render_template('users_am_membership.html', q=q)


class AmericaUserNZmembershipList(restful.Resource):
    
    def get(self):
        q = AmericaUserNZmembership.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        return render_template('usersusers_nz_membership_am.html', q=q)


class AmericaMetadata_AmericaList(restful.Resource):
    
    def get(self):
        q = AmericaMetadata_America.query.all()  
        #import jsonpickle
        #j = jsonpickle.encode(q)
        #return j
        return render_template('metadata_america.html', q=q)

