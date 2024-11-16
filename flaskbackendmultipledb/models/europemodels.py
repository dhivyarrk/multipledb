from .database import db
class Seller(db.Model):
    __bind_key__ = 'asia_database'
    __tablename__ = 'seller'

    seller_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    seller_name = db.Column(db.String(), unique=True, nullable=False)
    join_date = db.Column(db.Date, nullable=False)


class User(db.Model):
    __bind_key__ = 'asia_database'
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), nullable=False)
    membership_type = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date, nullable=False)


class Generic_Products(db.Model):
    __bind_key__ = 'asia_database'
    __tablename__ = 'generic_products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=False)
    availability = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)



class Reginol_Products(db.Model):
    __bind_key__ = 'asia_database'
    __tablename__ = 'reginol_products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False)
    price = db.Column(db.String(), nullable=False)
    availability = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('sellers.id'), nullable=False)


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)