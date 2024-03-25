"""Renaming product to supplier product

Revision ID: d0781c663473
Revises: e2f885cd8379
Create Date: 2024-03-25 21:44:03.066888

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd0781c663473'
down_revision: Union[str, None] = 'e2f885cd8379'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('suppliers', 'product', new_column_name= 'supplier_product')

def downgrade() -> None:
    op.alter_column('suppliers', 'supplier_product', new_column_name='product')
