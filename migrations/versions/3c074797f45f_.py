"""Initial DB Creation

Revision ID: 3c074797f45f
Revises: None
Create Date: 2016-10-26 21:52:16.959265

"""

# revision identifiers, used by Alembic.
revision = '3c074797f45f'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog_post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('datetimeposted', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_post')
    ### end Alembic commands ###
