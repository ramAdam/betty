"""initial database migragtion

Revision ID: 8160b6521bff
Revises: 
Create Date: 2019-09-02 03:26:43.881928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8160b6521bff'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email_on', sa.String(), nullable=False),
    sa.Column('registered_on', sa.DateTime(), nullable=False),
    sa.Column('user_name', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_on'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('User')
    # ### end Alembic commands ###
