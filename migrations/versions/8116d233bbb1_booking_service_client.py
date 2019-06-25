"""Booking, Service, Client

Revision ID: 8116d233bbb1
Revises: 868fa28893da
Create Date: 2018-06-10 07:21:51.842941

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8116d233bbb1'
down_revision = '868fa28893da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=40), nullable=False),
    sa.Column('lname', sa.String(length=40), nullable=False),
    sa.Column('phone', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_cancel', sa.Boolean(), nullable=True),
    sa.Column('cancelation_reason', sa.String(length=200), nullable=True),
    sa.Column('booked_datetime', sa.DateTime(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('end_time', sa.DateTime(), nullable=True),
    sa.Column('total_price', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('service_booked',
    sa.Column('booking_id', sa.Integer(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['booking.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], )
    )
    op.create_table('service_provided',
    sa.Column('booking_id', sa.Integer(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['booking_id'], ['booking.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_provided')
    op.drop_table('service_booked')
    op.drop_table('booking')
    op.drop_table('service')
    op.drop_table('client')
    # ### end Alembic commands ###
