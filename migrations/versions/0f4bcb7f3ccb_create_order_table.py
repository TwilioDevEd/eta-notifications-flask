"""create order table

Revision ID: 0f4bcb7f3ccb
Revises:
Create Date: 2016-02-18 16:00:29.344025

"""

# revision identifiers, used by Alembic.
revision = '0f4bcb7f3ccb'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('customer_name', sa.String(50), nullable=False),
        sa.Column('customer_phone_number', sa.String(20), nullable=False),
        sa.Column('status', sa.String(20), nullable=False, server_default='Ready'),
        sa.Column('notification_status', sa.String(20), nullable=False, server_default='None')
    )

def downgrade():
    op.drop_table('orders')
