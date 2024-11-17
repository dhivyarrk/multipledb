from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS
from flaskbackendmultipledb.config import MultidbConfig
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.americamodels import AmericaUserAM, AmericaUserNZ, AmericaGenericProducts, AmericaRegionalProducts, AmericaUserAMmembership, AmericaUserNZmembership, AmericaMetadata_America
from flaskbackendmultipledb.models.europemodels import EuropeUserAM, EuropUserNZ, EuropeGenericProducts, EuropeRegionalProducts, EuropeUserAMmembership, EuropeUserNZmembership, EuropeMetadata_Europe
from flaskbackendmultipledb.models.asiamodels import AsiaUserAM, AsiaUserNZ, AsiaGenericProducts, AsiaRegionalProducts, AsiaUserAMmembership, AsiaUserNZmembership
from flaskbackendmultipledb.modules.asiaviews import AsiaUserAMList , AsiaUserNZList, AsiaGenericProductsList, AsiaRegionalProductsList, AsiaUserAMmembershipList, AsiaUserNZmembershipList
from flaskbackendmultipledb.modules.americaviews import AmericaUserAMList, AmericaUserNZList, AmericaGenericProductsList, AmericaRegionalProductsList, AmericaUserAMmembershipList, AmericaUserNZmembershipList, AmericaMetadata_AmericaList
from flaskbackendmultipledb.models.europemodels import EuropeUserAMList , EuropUserNZList, EuropeGenericProductsList, EuropeRegionalProductsList, EuropeUserAMmembershipList, EuropeUserNZmembershipList, EuropeMetadata_EuropeList
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(MultidbConfig)
    CORS(app, origins=['http://localhost:3000'])
    db.init_app(app)
    migrate = Migrate(app, db)
    api=Api(app)
    api.add_resource(AmericaUserAMList, '/america/usersam')
    api.add_resource(AmericaUserNZList, '/america/usersnz')
    api.add_resource(AmericaGenericProductsList, '/america/genericproducts')
    api.add_resource(AmericaRegionalProductsList, '/america/regionalproducts')
    api.add_resource(AmericaUserAMmembershipList, '/america/americauserammembership')
    api.add_resource(AmericaUserNZmembershipList, '/america/americausernzmembership')
    api.add_resource(AmericaMetadata_AmericaList, '/america/americametadata')
    
    return app