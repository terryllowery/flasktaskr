__author__ = 'terrylowery'

from views import db
from models import Task
from datetime import date


db.create_all()

# db.session.add(Task("Finish this tutorial", date(2013,3,13), 10, 1))
# db.session.add(Task("Finish real python", date(2016,12,16), 10, 1))


db.session.commit()