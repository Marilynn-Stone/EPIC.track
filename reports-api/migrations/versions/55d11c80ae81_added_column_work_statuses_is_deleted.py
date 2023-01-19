"""added column work_statuses.is_deleted

Revision ID: 55d11c80ae81
Revises: 5353dec70836
Create Date: 2022-12-26 09:34:17.758779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55d11c80ae81'
down_revision = '5353dec70836'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_statuses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_deleted', sa.Boolean(), nullable=True, default=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('work_statuses', schema=None) as batch_op:
        batch_op.drop_column('is_deleted')

    # ### end Alembic commands ###