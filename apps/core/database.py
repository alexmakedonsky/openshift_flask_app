from flask_sqlalchemy import SQLAlchemy
from contextlib import contextmanager

db = SQLAlchemy()


@contextmanager
def session_scope(commit=True, flush=True):
    """Provide a transactional scope around a series of operations."""
    try:
        yield db.session
        if commit:
            db.session.commit()
        elif flush:
            db.session.flush()
    except:
        db.session.rollback()
        raise Exception()


def read():
    return session_scope(commit=False, flush=False)


def write():
    return session_scope()


