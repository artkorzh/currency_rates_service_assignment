"""initial

Revision ID: b60814b24383
Revises: 
Create Date: 2022-10-27 14:55:46.553358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Sequence, CreateSequence


# revision identifiers, used by Alembic.
revision = "b60814b24383"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(CreateSequence(Sequence("symbols_id_seq")))

    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "symbols",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("symbol", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("symbol"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("symbols")
    # ### end Alembic commands ###
