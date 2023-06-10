"""first

Revision ID: d4e41e955df2
Revises: 773ed70e56d3
Create Date: 2023-06-10 05:17:17.073438

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4e41e955df2'
down_revision = '773ed70e56d3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('btc_coin',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('estimated_delivery_price', sa.Numeric(), nullable=False),
    sa.Column('index_price', sa.Numeric(), nullable=False),
    sa.Column('current_time', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_btc_coin'))
    )
    op.create_table('eth_coin',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('estimated_delivery_price', sa.Numeric(), nullable=False),
    sa.Column('index_price', sa.Numeric(), nullable=False),
    sa.Column('current_time', sa.Numeric(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_eth_coin'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('eth_coin')
    op.drop_table('btc_coin')
    # ### end Alembic commands ###
