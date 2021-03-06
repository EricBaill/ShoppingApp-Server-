"""empty message

Revision ID: 5e7b2738ed43
Revises: b1151f6adbb0
Create Date: 2019-04-15 14:16:42.139658

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5e7b2738ed43'
down_revision = 'b1151f6adbb0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('admin', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('carousel', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('orders', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('productions', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.alter_column('user', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('productions', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('orders', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('carousel', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    op.alter_column('admin', 'create_at',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###
