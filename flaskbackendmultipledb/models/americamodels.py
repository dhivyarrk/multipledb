from flaskbackendmultipledb.database import db

class AmericaUserAM(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'users_am'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date, nullable=False)

class AmericaUserNZ(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'users_nz'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(), nullable=False)
    join_date = db.Column(db.Date, nullable=False)


class AmericaGenericProducts(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'generic_products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False)
    product_description = db.Column(db.String(), nullable=False)


class AmericaRegionalProducts(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'regional_products'

    product_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(), nullable=False)
    product_description = db.Column(db.String(), nullable=False)
    

class AmericaUserAMmembership(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'users_am_membership'

    user_id = db.Column(db.Integer, db.ForeignKey('users_am.user_id'), primary_key=True, nullable=False)
    membership = db.Column(db.String(), nullable=False, default='regular')
    
    __table_args__ = (
        db.CheckConstraint(membership.in_(['regular', 'premium']), name='member_types'),
    )
   

class AmericaUserNZmembership(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'users_nz_membership'

    user_id = db.Column(db.Integer,  db.ForeignKey('users_nz.user_id'), primary_key=True, nullable=False)
    membership = db.Column(db.String(), nullable=False, default='regular')
    
    __table_args__ = (
        db.CheckConstraint(membership.in_(['regular', 'premium']), name='member_types'),
    )


class AmericaMetadata_America(db.Model):
    __bind_key__ = 'america_database'
    __tablename__ = 'metadata_america'

    metadata_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    metadata_info = db.Column(db.String(), nullable=False)