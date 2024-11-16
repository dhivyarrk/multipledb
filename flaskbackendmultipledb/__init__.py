from flask import Flask
from flask_migrate import Migrate
from flaskbackendmultipledb.config import MultidbConfig
from flaskbackendmultipledb.database import db
from flask_cors import CORS
from flaskbackendmultipledb.models.americamodels import AmericaUserAM, AmericaUserNZ, AmericaGenericProducts, AmericaRegionalProducts, AmericaUserAMmembership, AmericaUserNZmembership, AmericaMetadata_America
from flaskbackendmultipledb.models.europemodels import EuropeUserAM, EuropUserNZ, EuropeGenericProducts, EuropeRegionalProducts, EuropeUserAMmembership, EuropeUserNZmembership, EuropeMetadata_Europe
from flaskbackendmultipledb.models.asiamodels import AsiaUserAM, AsiaUserNZ, AsiaGenericProducts, AsiaRegionalProducts, AsiaUserAMmembership, AsiaUserNZmembership
def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "Miy_Secret_Key"
    )
    app.config.from_object(MultidbConfig)
    CORS(app, origins=['http://localhost:3000'])
    db.init_app(app)
    migrate = Migrate(app, db)
    return app