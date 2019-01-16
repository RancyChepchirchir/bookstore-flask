"""add flat number to loc model

Revision ID: 4e8c2eb9ae96
Revises: 28c03e139752
Create Date: 2019-01-11 19:01:02.312242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e8c2eb9ae96'
down_revision = '28c03e139752'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('location', sa.Column('flat_number', sa.String(length=8), nullable=True))
    op.drop_index('location_index', table_name='location')
    op.create_index('location_index', 'location', ['place', 'street_name', 'street_number', 'flat_number'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('location_index', table_name='location')
    op.create_index('location_index', 'location', ['place', 'street_name', 'street_number'], unique=False)
    op.drop_column('location', 'flat_number')
    # ### end Alembic commands ###
