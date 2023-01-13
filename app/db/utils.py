from sqlalchemy import DDL, event

from app.core.config import DATABASE_SCHEMA as schema
from app.db.session import get_db


def ping_db():
    db = next(get_db())
    db.execute("SELECT 1")


def create_trigger_for_update(table: str):

    return DDL(
        """
    CREATE TRIGGER set_timestamp
    BEFORE UPDATE ON {0}.{1}
    FOR EACH ROW
    EXECUTE PROCEDURE trigger_set_timestamp();
    """.format(
            schema, table
        )
    )
