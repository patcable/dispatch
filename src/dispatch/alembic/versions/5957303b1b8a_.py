"""Adds additional columns to incident priorities.

Revision ID: 5957303b1b8a
Revises: 5d4dee3e24fc
Create Date: 2020-04-02 12:28:37.346419

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = "5957303b1b8a"
down_revision = "5d4dee3e24fc"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("incident_priority", sa.Column("page_commander", sa.Boolean(), nullable=True))
    op.add_column(
        "incident_priority",
        sa.Column("search_vector", sqlalchemy_utils.types.ts_vector.TSVectorType(), nullable=True),
    )
    op.add_column("incident_priority", sa.Column("view_order", sa.Integer(), nullable=True))
    op.create_index(
        "ix_incident_priority_search_vector",
        "incident_priority",
        ["search_vector"],
        unique=False,
        postgresql_using="gin",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_incident_priority_search_vector", table_name="incident_priority")
    op.drop_column("incident_priority", "view_order")
    op.drop_column("incident_priority", "search_vector")
    op.drop_column("incident_priority", "page_commander")
    # ### end Alembic commands ###
