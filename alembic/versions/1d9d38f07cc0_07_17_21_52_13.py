"""07-17:21:52:13

Revision ID: 1d9d38f07cc0
Revises: 8e152eb8f2fb
Create Date: 2023-07-17 15:52:21.422557

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d9d38f07cc0'
down_revision = '8e152eb8f2fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'description',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('products', 'type',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'origin',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'certification',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'color',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('products', 'price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'price',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               nullable=False)
    op.alter_column('products', 'color',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'certification',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'origin',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'type',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('products', 'description',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('products', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###