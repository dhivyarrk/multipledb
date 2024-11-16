from flask import Flask
from flask_migrate import Migrate
from flask_restful import Resource, Api
from flask_cors import CORS
from flaskbackendmultipledb.config import MultidbConfig
from flaskbackendmultipledb.database import db
from flaskbackendmultipledb.models.americamodels import AmericaUserAM, AmericaUserNZ, AmericaGenericProducts, AmericaRegionalProducts, AmericaUserAMmembership, AmericaUserNZmembership, AmericaMetadata_America
from flaskbackendmultipledb.models.europemodels import EuropeUserAM, EuropUserNZ, EuropeGenericProducts, EuropeRegionalProducts, EuropeUserAMmembership, EuropeUserNZmembership, EuropeMetadata_Europe
from flaskbackendmultipledb.models.asiamodels import AsiaUserAM, AsiaUserNZ, AsiaGenericProducts, AsiaRegionalProducts, AsiaUserAMmembership, AsiaUserNZmembership
from flaskbackendmultipledb.modules.asiaviews import AsiaUserAMList
from flaskbackendmultipledb.modules.americaviews import AmericaUserAMList, AmericaUserNZmembershipList, AmericaGenericProductsList, AmericaRegionalProductsList, AmericaUserAMmembershipList, AmericaUserNZmembershipList, AmericaMetadata_AmericaList
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
    api.add_resource(AmericaGenericProductsList, '/america/usersam')
    api.add_resource(AmericaRegionalProductsList, '/america/usersam')
    api.add_resource(AmericaUserAMmembershipList, '/america/usersam')
    api.add_resource(AmericaUserNZmembershipList, '/america/usersam')
    api.add_resource(AmericaMetadata_AmericaList, '/america/usersam')
    return app