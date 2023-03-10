"""comment2

Revision ID: 9166f4c7a4c8
Revises: 79aeb8c935e9
Create Date: 2022-11-17 11:20:34.738037

"""
from alembic import op
import sqlalchemy as sa

from sqlalchemy import event, DDL


# revision identifiers, used by Alembic.
revision = '9166f4c7a4c8'
down_revision = '79aeb8c935e9'
branch_labels = None
depends_on = None


func_ = DDL("""
    CREATE OR REPLACE FUNCTION trigger_set_timestamp()
    RETURNS TRIGGER AS $$
    BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
""")


trig_ = DDL("""
    CREATE TRIGGER set_timestamp
    BEFORE UPDATE ON todos
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();
""")


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column(
        'completed_at_abc', sa.TIMESTAMP(), nullable=True))
    # ### end Alembic commands ###
    op.execute(func_)
    op.execute(trig_)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed_at_abc')
    # ### end Alembic commands ###
