"""empty message

Revision ID: 6c66cff79ca8
Revises: bbe5653974c8
Create Date: 2020-05-15 15:49:03.348791

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6c66cff79ca8'
down_revision = 'bbe5653974c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('role', sa.Column('time', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('role', 'time')
    # ### end Alembic commands ###
