"""special fields

Revision ID: 03791c319e2b
Revises: 7a42d4f57279
Create Date: 2023-12-01 12:39:54.325967

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '03791c319e2b'
down_revision = '7a42d4f57279'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('special_fields',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('entity', sa.Enum('PROJECT', 'PROPONENT', 'WORK', name='entityenum'), nullable=False),
    sa.Column('entity_id', sa.Integer(), nullable=False),
    sa.Column('field_name', sa.String(length=100), nullable=False),
    sa.Column('field_value', sa.String(), nullable=False),
    sa.Column('time_range', postgresql.TSTZRANGE(), nullable=False),
    sa.Column('created_by', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text("TIMEZONE('utc', CURRENT_TIMESTAMP)"), nullable=True),
    sa.Column('updated_by', sa.String(length=255), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('is_active', sa.Boolean(), server_default='t', nullable=False),
    sa.Column('is_deleted', sa.Boolean(), server_default='f', nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('special_fields', schema=None) as batch_op:
        batch_op.create_index('entity_field_index', ['entity', 'entity_id', 'field_name', 'time_range'], unique=False)

    op.create_table('special_fields_history',
    sa.Column('id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('entity', sa.Enum('PROJECT', 'PROPONENT', 'WORK', name='entityenum'), autoincrement=False, nullable=False),
    sa.Column('entity_id', sa.Integer(), autoincrement=False, nullable=False),
    sa.Column('field_name', sa.String(length=100), autoincrement=False, nullable=False),
    sa.Column('field_value', sa.String(), autoincrement=False, nullable=False),
    sa.Column('time_range', postgresql.TSTZRANGE(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.String(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.String(length=255), autoincrement=False, nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.Boolean(), autoincrement=False, nullable=False),
    sa.Column('is_deleted', sa.Boolean(), autoincrement=False, nullable=False),
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('during', postgresql.TSTZRANGE(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'pk')
    )
    with op.batch_alter_table('special_fields_history', schema=None) as batch_op:
        batch_op.create_index('entity_field_history_index', ['entity', 'entity_id', 'field_name', 'time_range'], unique=False)

    op.drop_table('project_special_fields')
    with op.batch_alter_table('event_templates', schema=None) as batch_op:
        batch_op.alter_column('visibility',
               existing_type=postgresql.ENUM('MANDATORY', 'OPTIONAL', 'HIDDEN', name='eventtemplatevisibilityenum'),
               comment='Indicate whether the event generated with this template should be        autogenerated  or available for optional events or added in the back end using actions',
               existing_comment='Indicate whether the event generated with this template should be autogenerated  or available for optional events or added in the back end using actions',
               existing_nullable=False)

    with op.batch_alter_table('event_templates_history', schema=None) as batch_op:
        batch_op.alter_column('visibility',
               existing_type=postgresql.ENUM('MANDATORY', 'OPTIONAL', 'HIDDEN', name='eventtemplatevisibilityenum'),
               comment='Indicate whether the event generated with this template should be        autogenerated  or available for optional events or added in the back end using actions',
               existing_comment='Indicate whether the event generated with this template should be autogenerated  or available for optional events or added in the back end using actions',
               existing_nullable=False,
               autoincrement=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('event_templates_history', schema=None) as batch_op:
        batch_op.alter_column('visibility',
               existing_type=postgresql.ENUM('MANDATORY', 'OPTIONAL', 'HIDDEN', name='eventtemplatevisibilityenum'),
               comment='Indicate whether the event generated with this template should be autogenerated  or available for optional events or added in the back end using actions',
               existing_comment='Indicate whether the event generated with this template should be        autogenerated  or available for optional events or added in the back end using actions',
               existing_nullable=False,
               autoincrement=False)

    with op.batch_alter_table('event_templates', schema=None) as batch_op:
        batch_op.alter_column('visibility',
               existing_type=postgresql.ENUM('MANDATORY', 'OPTIONAL', 'HIDDEN', name='eventtemplatevisibilityenum'),
               comment='Indicate whether the event generated with this template should be autogenerated  or available for optional events or added in the back end using actions',
               existing_comment='Indicate whether the event generated with this template should be        autogenerated  or available for optional events or added in the back end using actions',
               existing_nullable=False)

    op.create_table('project_special_fields',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('field_name', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('field_value', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('time_range', postgresql.TSTZRANGE(), autoincrement=False, nullable=False),
    sa.Column('project_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("timezone('utc'::text, CURRENT_TIMESTAMP)"), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), server_default=sa.text('true'), autoincrement=False, nullable=False),
    sa.Column('is_deleted', sa.BOOLEAN(), server_default=sa.text('false'), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='project_special_fields_project_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='project_special_fields_pkey')
    )
    with op.batch_alter_table('special_fields_history', schema=None) as batch_op:
        batch_op.drop_index('entity_field_history_index')

    op.drop_table('special_fields_history')
    with op.batch_alter_table('special_fields', schema=None) as batch_op:
        batch_op.drop_index('entity_field_index')

    op.drop_table('special_fields')
    # ### end Alembic commands ###