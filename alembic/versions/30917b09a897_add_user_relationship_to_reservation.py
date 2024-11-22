"""Add user relationship to Reservation

Revision ID: 30917b09a897
Revises: b4ebaa9400c1
Create Date: 2024-11-22 09:41:45.309024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '30917b09a897'
down_revision = 'b4ebaa9400c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###