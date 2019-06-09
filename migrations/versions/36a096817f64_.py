"""empty message

Revision ID: 36a096817f64
Revises: 75668b1f28e3
Create Date: 2019-06-08 22:20:01.320660

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '36a096817f64'
down_revision = '75668b1f28e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('address', sa.String(length=120), nullable=False))
    op.add_column('person', sa.Column('city', sa.String(length=120), nullable=False))
    op.add_column('person', sa.Column('state', sa.String(length=120), nullable=False))
    op.add_column('person', sa.Column('zip_code', sa.String(length=120), nullable=False))
    op.drop_index('email', table_name='person')
    op.create_unique_constraint(None, 'person', ['state'])
    op.create_unique_constraint(None, 'person', ['zip_code'])
    op.create_unique_constraint(None, 'person', ['address'])
    op.create_unique_constraint(None, 'person', ['city'])
    op.drop_column('person', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('email', mysql.VARCHAR(length=120), nullable=False))
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    op.drop_constraint(None, 'person', type_='unique')
    op.create_index('email', 'person', ['email'], unique=True)
    op.drop_column('person', 'zip_code')
    op.drop_column('person', 'state')
    op.drop_column('person', 'city')
    op.drop_column('person', 'address')
    # ### end Alembic commands ###
