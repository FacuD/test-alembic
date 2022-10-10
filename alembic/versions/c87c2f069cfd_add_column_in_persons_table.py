"""Add column in persons table

Revision ID: c87c2f069cfd
Revises: 635e3b748320
Create Date: 2022-10-09 21:20:56.697002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "c87c2f069cfd"
down_revision = "635e3b748320"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("persons", sa.Column("age", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("persons", "age")
