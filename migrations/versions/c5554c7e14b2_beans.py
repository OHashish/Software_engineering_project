"""beans

Revision ID: c5554c7e14b2
Revises: 
Create Date: 2021-03-27 15:18:41.405702

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5554c7e14b2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movie',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('blurb', sa.String(length=1000), nullable=True),
    sa.Column('director', sa.String(length=80), nullable=True),
    sa.Column('cast', sa.String(length=100), nullable=True),
    sa.Column('certificate', sa.String(length=20), nullable=True),
    sa.Column('runtime', sa.Integer(), nullable=True),
    sa.Column('movie_poster', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('screen',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.Column('screen_time', sa.DateTime(), nullable=True),
    sa.Column('movie_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ticket',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('screen_id', sa.Integer(), nullable=True),
    sa.Column('age_type', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['screen_id'], ['screen.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('seat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(length=80), nullable=True),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('ticket_id', sa.Integer(), nullable=True),
    sa.Column('screen_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['screen_id'], ['screen.id'], ),
    sa.ForeignKeyConstraint(['ticket_id'], ['ticket.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seat')
    op.drop_table('ticket')
    op.drop_table('screen')
    op.drop_table('user')
    op.drop_table('movie')
    # ### end Alembic commands ###
