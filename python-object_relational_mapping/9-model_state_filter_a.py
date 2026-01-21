#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects, sorted by id in ascending order
    states = session.query(State).where(State.id != 4).order_by(State.id).all()

    # Display the results
    if not states:
        print("Nothing")
    else:
        for state in states:
            print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
