"""create customers

Revision ID: 45fae6c1015e
Revises: 
Create Date: 2022-09-02 17:32:18.095531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45fae6c1015e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE TABLE customers(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL
        );
        """
    )


def downgrade():
    op.execute(
        """
        DROP TABLE customers;
        """
    )
