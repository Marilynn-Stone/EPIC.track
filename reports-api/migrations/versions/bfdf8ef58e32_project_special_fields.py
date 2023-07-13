"""project special fields

Revision ID: bfdf8ef58e32
Revises: fffde480809a
Create Date: 2023-07-12 11:08:27.092278

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bfdf8ef58e32'
down_revision = 'fffde480809a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_special_fields',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('field_name', sa.String(length=100), nullable=False),
    sa.Column('field_value', sa.String(), nullable=False),
    sa.Column('time_range', postgresql.TSTZRANGE(), nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_special_fields')
    # ### end Alembic commands ###
