"""empty message

Revision ID: 59e5df6a489
Revises: 1d461753b2e
Create Date: 2015-10-01 10:20:20.477186

"""

# revision identifiers, used by Alembic.
revision = '59e5df6a489'
down_revision = None
depends_on = '1d461753b2e'

# add this here in order to use revision with branch_label
branch_labels = ('beavy.comments', )

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('objects', sa.Column('in_reply_to_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'objects', 'objects', ['in_reply_to_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'objects', type_='foreignkey')
    op.drop_column('objects', 'in_reply_to_id')
    ### end Alembic commands ###