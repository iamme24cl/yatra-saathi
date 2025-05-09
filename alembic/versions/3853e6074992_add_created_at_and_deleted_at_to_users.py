"""Add created_at and deleted_at to users

Revision ID: 3853e6074992
Revises: 729c493581f6
Create Date: 2025-03-30 19:17:54.805770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3853e6074992'
down_revision: Union[str, None] = '729c493581f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('drivers', 'vehicle_info',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               comment='Vehicle info as JSON: type, model, year, passenger_capacity, license_number',
               existing_nullable=True)
    op.add_column('users', sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True))
    op.add_column('users', sa.Column('deleted_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'deleted_at')
    op.drop_column('users', 'created_at')
    op.alter_column('drivers', 'vehicle_info',
               existing_type=postgresql.JSON(astext_type=sa.Text()),
               comment=None,
               existing_comment='Vehicle info as JSON: type, model, year, passenger_capacity, license_number',
               existing_nullable=True)
    # ### end Alembic commands ###
