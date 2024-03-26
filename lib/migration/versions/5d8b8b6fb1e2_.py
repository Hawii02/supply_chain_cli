"""empty message

Revision ID: 5d8b8b6fb1e2
Revises: d0781c663473
Create Date: 2024-03-26 10:48:31.686719

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5d8b8b6fb1e2'
down_revision: Union[str, None] = 'd0781c663473'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
