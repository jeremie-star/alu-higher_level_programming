#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter a
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    # Create the engine with database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query and delete all states with 'a' in their name
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()
        if states_to_delete:
            for state in states_to_delete:
                session.delete(state)

            session.commit()  # Commit the transaction
        else:
            print("No states found with 'a' in their name.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        session.close()  # Always close the session

