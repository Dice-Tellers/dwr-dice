import random as rnd

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class DiceSet(db.Model):
    __tablename__ = 'diceset'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Unicode(128), nullable=False)

    def to_json(self):
        dice = Die.query.filter_by(id_set=self.id).all()
        return {'id': self.id, 'name': self.name,
                'dice': [die.to_json() for die in dice]}

    def roll_set(self, dice_number):
        dice_indexes = rnd.sample(range(1, 7), dice_number)
        dice = Die.query.filter(and_(Die.id_set == self.id, Die.number.in_(dice_indexes)))

        return [die.roll_die() for die in dice]


class Die(db.Model):
    __tablename__ = 'die'

    number = db.Column(db.Integer, primary_key=True)
    id_set = db.Column(db.Integer, db.ForeignKey('diceset.id'), primary_key=True)
    figures = db.Column(db.Unicode(128), nullable=False)
    dice_set = relationship('DiceSet', foreign_keys='Die.id_set')

    def figures_to_array(self):
        return (self.figures.split('#'))[1:-1]

    def roll_die(self):
        return {self.number: rnd.choice(self.figures_to_array())}

    def to_json(self):
        return {'number': self.number, 'figures': self.figures_to_array()}
