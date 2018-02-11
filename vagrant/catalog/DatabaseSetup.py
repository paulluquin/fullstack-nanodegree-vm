from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

# Setup User Table
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))


# Setup Item Table
class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    description = Column(String(250), nullable=True)
    location = Column(String(100))
    price = Column (Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    picture = Column(String(250), nullable=True)

    car_option = relationship('CarOption', cascade='all, delete-orphan')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.brand,
            'model': self.model,
            'description': self.description,
            'location': self.location,
            'price': self.price,
            'user_id': self.user_id,
            'picture': self.picture
        }

class CarOption(Base):
    __tablename__ = 'car_options'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    car_id = Column(Integer, ForeignKey('cars.id'))
    car = relationship(Car)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'car_id': self.car_id,
            'user_id': self.user_id,
            'picture': self.picture,
        }


engine = create_engine('sqlite:///DealershipInventory.db')


Base.metadata.create_all(engine)
