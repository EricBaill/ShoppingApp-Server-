"""empty message

Revision ID: 0d89263ca581
Revises: 6ac1d3539722
Create Date: 2019-03-27 11:18:43.287922

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d89263ca581'
down_revision = '6ac1d3539722'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('is_remove', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'is_remove')
    # ### end Alembic commands ###
