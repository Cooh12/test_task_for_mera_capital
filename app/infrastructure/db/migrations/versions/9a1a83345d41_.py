"""

Revision ID: 9a1a83345d41
Revises: 6bc5d5a34512
Create Date: 2023-06-12 18:09:25.340003

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a1a83345d41'
down_revision = '6bc5d5a34512'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coins',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('coin_name', sa.Text(), nullable=False),
    sa.Column('estimated_delivery_price', sa.Numeric(), nullable=False),
    sa.Column('index_price', sa.Numeric(), nullable=False),
    sa.Column('created_at', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_coins'))
    )
    op.drop_table('btc_coin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('btc_coin',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('coin_name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('estimated_delivery_price', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('index_price', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.NUMERIC(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='pk_btc_coin')
    )
    op.drop_table('coins')
    # ### end Alembic commands ###
