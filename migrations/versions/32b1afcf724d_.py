"""empty message

Revision ID: 32b1afcf724d
Revises: 01bc7843d696
Create Date: 2016-12-30 14:01:24.416473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32b1afcf724d'
down_revision = '01bc7843d696'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('check', sa.Column('parent_check_id', sa.Integer(), nullable=True))
    op.add_column('check', sa.Column('read_only', sa.Boolean()))
    op.execute('update "check" set read_only = false')
    op.alter_column('check', 'read_only', nullable=False)
    op.add_column('data_source', sa.Column('parent_data_source_id', sa.Integer(), nullable=True))
    op.add_column('data_source', sa.Column('read_only', sa.Boolean()))
    op.execute('update data_source set read_only = false')
    op.alter_column('data_source', 'read_only', nullable=False)
    op.add_column('job_template', sa.Column('parent_job_template_id', sa.Integer(), nullable=True))
    op.add_column('job_template', sa.Column('read_only', sa.Boolean()))
    op.execute('update job_template set read_only = false')
    op.alter_column('job_template', 'read_only', nullable=False)
    op.add_column('rule', sa.Column('parent_rule_id', sa.Integer(), nullable=True))
    op.add_column('rule', sa.Column('read_only', sa.Boolean()))
    op.execute('update rule set read_only = false')
    op.alter_column('rule', 'read_only', nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rule', 'read_only')
    op.drop_column('rule', 'parent_rule_id')
    op.drop_column('job_template', 'read_only')
    op.drop_column('job_template', 'parent_job_template_id')
    op.drop_column('data_source', 'read_only')
    op.drop_column('data_source', 'parent_data_source_id')
    op.drop_column('check', 'read_only')
    op.drop_column('check', 'parent_check_id')
    # ### end Alembic commands ###