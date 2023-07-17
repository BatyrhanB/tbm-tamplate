"""07-17:21:47:36

Revision ID: 8e152eb8f2fb
Revises: 3da4de1789be
Create Date: 2023-07-17 15:47:45.911750

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e152eb8f2fb'
down_revision = '3da4de1789be'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('categories', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'origin',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'certification',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'color',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    op.alter_column('products', 'color',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'certification',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'origin',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('categories', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###