"""new field in user model

Revision ID: 646d7b7c5c83
Revises: 68abf5a44be5
Create Date: 2019-01-03 19:14:27.783494

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '646d7b7c5c83'
down_revision = '68abf5a44be5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
