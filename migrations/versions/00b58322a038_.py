"""empty message

Revision ID: 00b58322a038
Revises: 0d89263ca581
Create Date: 2019-04-04 13:05:40.311253

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '00b58322a038'
down_revision = '0d89263ca581'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('productions', 'cover_img',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.drop_column('productions', 'name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('productions', sa.Column('name', mysql.VARCHAR(length=256), nullable=False))
    op.alter_column('productions', 'cover_img',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###
