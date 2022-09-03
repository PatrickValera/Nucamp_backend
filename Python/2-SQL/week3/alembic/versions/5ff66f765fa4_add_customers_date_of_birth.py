"""add customers date_of_birth

Revision ID: 5ff66f765fa4
Revises: 45fae6c1015e
Create Date: 2022-09-02 17:37:25.646622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ff66f765fa4'
down_revision = '45fae6c1015e'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        ALTER TABLE customers
        ADD COLUMN date_of_birth TIMESTAMP;
        """
    )

def downgrade():
    op.execute(
        """
        ALTER TABLE customers
        DROP COLUMN date_of_birth;
        """
    )
