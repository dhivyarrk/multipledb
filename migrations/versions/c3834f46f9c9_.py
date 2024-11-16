"""empty message

Revision ID: c3834f46f9c9
Revises: 
Create Date: 2024-11-16 22:23:41.758698

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3834f46f9c9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_asia_database():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('generic_products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('regional_products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('users_am',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('join_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_nz',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('join_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_am_membership',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership', sa.String(), nullable=False),
    sa.CheckConstraint("membership IN ('regular', 'premium')", name='member_types'),
    sa.ForeignKeyConstraint(['user_id'], ['users_am.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_nz_membership',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership', sa.String(), nullable=False),
    sa.CheckConstraint("membership IN ('regular', 'premium')", name='member_types'),
    sa.ForeignKeyConstraint(['user_id'], ['users_nz.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade_asia_database():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_nz_membership')
    op.drop_table('users_am_membership')
    op.drop_table('users_nz')
    op.drop_table('users_am')
    op.drop_table('regional_products')
    op.drop_table('generic_products')
    # ### end Alembic commands ###


def upgrade_europe_database():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('generic_products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('metadata_europe',
    sa.Column('metadata_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('metadata_info', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('metadata_id')
    )
    op.create_table('regional_products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('users_am',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('join_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_nz',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('join_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_am_membership',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership', sa.String(), nullable=False),
    sa.CheckConstraint("membership IN ('regular', 'premium')", name='member_types'),
    sa.ForeignKeyConstraint(['user_id'], ['users_am.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_nz_membership',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership', sa.String(), nullable=False),
    sa.CheckConstraint("membership IN ('regular', 'premium')", name='member_types'),
    sa.ForeignKeyConstraint(['user_id'], ['users_nz.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade_europe_database():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_nz_membership')
    op.drop_table('users_am_membership')
    op.drop_table('users_nz')
    op.drop_table('users_am')
    op.drop_table('regional_products')
    op.drop_table('metadata_europe')
    op.drop_table('generic_products')
    # ### end Alembic commands ###


def upgrade_america_database():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('generic_products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('metadata_america',
    sa.Column('metadata_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('metadata_info', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('metadata_id')
    )
    op.create_table('regional_products',
    sa.Column('product_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('product_description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('product_id')
    )
    op.create_table('users_am',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('join_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_nz',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.Column('join_date', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_am_membership',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership', sa.String(), nullable=False),
    sa.CheckConstraint("membership IN ('regular', 'premium')", name='member_types'),
    sa.ForeignKeyConstraint(['user_id'], ['users_am.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('users_nz_membership',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('membership', sa.String(), nullable=False),
    sa.CheckConstraint("membership IN ('regular', 'premium')", name='member_types'),
    sa.ForeignKeyConstraint(['user_id'], ['users_nz.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade_america_database():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_nz_membership')
    op.drop_table('users_am_membership')
    op.drop_table('users_nz')
    op.drop_table('users_am')
    op.drop_table('regional_products')
    op.drop_table('metadata_america')
    op.drop_table('generic_products')
    # ### end Alembic commands ###

