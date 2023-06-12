from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name.like(name)).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id.is_(id)).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.breed.is_(breed),
                                     Dog.name.like(name)).first()

def update_breed(session, dog, breed):
    session.query(Dog).filter(Dog.name.is_(dog.name)).update({Dog.breed: breed})