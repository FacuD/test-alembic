"""Create persons table

Revision ID: 635e3b748320
Revises: 
Create Date: 2022-10-09 21:06:39.585530

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Column, Integer, String, DateTime


# revision identifiers, used by Alembic.
revision = "635e3b748320"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "persons",
        Column("id", Integer, primary_key=True),
        Column("name", String(255), nullable=False),
        Column("birthday", DateTime, nullable=False),
        Column("created_at", DateTime, nullable=False),
        Column("updated_at", DateTime, nullable=False),
    )


def downgrade() -> None:
    op.drop_table("persons")
