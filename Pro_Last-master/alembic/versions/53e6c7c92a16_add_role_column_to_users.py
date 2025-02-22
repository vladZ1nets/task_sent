"""Add role column to users

Revision ID: 53e6c7c92a16
Revises: 69ea4de712dc
Create Date: 2024-11-24 12:30:13.514923

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53e6c7c92a16'
down_revision: Union[str, None] = '69ea4de712dc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contracts', 'signed_datetime')
    op.alter_column('favorites', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('favorites', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('feedback', 'timestamp')
    op.add_column('users', sa.Column('role', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    op.add_column('feedback', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    op.alter_column('favorites', 'item_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('favorites', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('contracts', sa.Column('signed_datetime', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###
