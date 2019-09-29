"""added token blacked out

Revision ID: 27549b271e95
Revises: 8f34c7f76696
Create Date: 2019-09-18 18:11:28.914561

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27549b271e95'
down_revision = '8f34c7f76696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('BlackListToken',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_unique_constraint(None, 'User', ['public_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'User', type_='unique')
    op.drop_table('BlackListToken')
    # ### end Alembic commands ###