"""user rewards added columns

Revision ID: 418c31125764
Revises: 7be69ae2a07a
Create Date: 2022-11-23 13:22:05.995359

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '418c31125764'
down_revision = '7be69ae2a07a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('employement_rewards_employement_id_fkey', 'employement_rewards', type_='foreignkey')
    op.drop_constraint('employement_rewards_reward_id_fkey', 'employement_rewards', type_='foreignkey')
    op.create_foreign_key(None, 'employement_rewards', 'rewards', ['reward_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.create_foreign_key(None, 'employement_rewards', 'employements', ['employement_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.drop_constraint('rewards_employement_id_fkey', 'rewards', type_='foreignkey')
    op.create_foreign_key(None, 'rewards', 'employements', ['employement_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.add_column('user_rewards', sa.Column('citation_id', postgresql.UUID(), nullable=False))
    op.add_column('user_rewards', sa.Column('certificate', sa.Text(), nullable=True))
    op.add_column('user_rewards', sa.Column('is_uploaded', sa.Boolean(), server_default=sa.text('false'), nullable=False))
    op.drop_constraint('user_rewards_user_id_fkey', 'user_rewards', type_='foreignkey')
    op.drop_constraint('user_rewards_reward_id_fkey', 'user_rewards', type_='foreignkey')
    op.create_foreign_key(None, 'user_rewards', 'users', ['user_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.create_foreign_key(None, 'user_rewards', 'rewards', ['reward_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.create_foreign_key(None, 'user_rewards', 'users', ['citation_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.drop_constraint('users_employement_id_fkey', 'users', type_='foreignkey')
    op.drop_constraint('users_group_id_fkey', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'groups', ['group_id'], ['id'], source_schema='dev', referent_schema='dev')
    op.create_foreign_key(None, 'users', 'employements', ['employement_id'], ['id'], source_schema='dev', referent_schema='dev')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', schema='dev', type_='foreignkey')
    op.drop_constraint(None, 'users', schema='dev', type_='foreignkey')
    op.create_foreign_key('users_group_id_fkey', 'users', 'groups', ['group_id'], ['id'])
    op.create_foreign_key('users_employement_id_fkey', 'users', 'employements', ['employement_id'], ['id'])
    op.drop_constraint(None, 'user_rewards', schema='dev', type_='foreignkey')
    op.drop_constraint(None, 'user_rewards', schema='dev', type_='foreignkey')
    op.drop_constraint(None, 'user_rewards', schema='dev', type_='foreignkey')
    op.create_foreign_key('user_rewards_reward_id_fkey', 'user_rewards', 'rewards', ['reward_id'], ['id'])
    op.create_foreign_key('user_rewards_user_id_fkey', 'user_rewards', 'users', ['user_id'], ['id'])
    op.drop_column('user_rewards', 'is_uploaded')
    op.drop_column('user_rewards', 'certificate')
    op.drop_column('user_rewards', 'citation_id')
    op.drop_constraint(None, 'rewards', schema='dev', type_='foreignkey')
    op.create_foreign_key('rewards_employement_id_fkey', 'rewards', 'employements', ['employement_id'], ['id'])
    op.drop_constraint(None, 'employement_rewards', schema='dev', type_='foreignkey')
    op.drop_constraint(None, 'employement_rewards', schema='dev', type_='foreignkey')
    op.create_foreign_key('employement_rewards_reward_id_fkey', 'employement_rewards', 'rewards', ['reward_id'], ['id'])
    op.create_foreign_key('employement_rewards_employement_id_fkey', 'employement_rewards', 'employements', ['employement_id'], ['id'])
    # ### end Alembic commands ###
