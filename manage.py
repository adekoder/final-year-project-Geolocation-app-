import string
import random
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy.exc import SQLAlchemyError
from app import create_app, db
from app.models import Category, Location

app = create_app('default')
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def create_db():
    db.create_all()

@manager.command
def runtest():
    import unittest
    test = unittest.TestLoader().discover('test')
    unittest.TextTestRunner(verbosity=2).run(test)

@manager.command
def seed_categories_data():
    category_ids = ('cat-1234', 'cat-1256', 'cat-3456', 'cat-5678', 'cat-3443')
    category_names  = ('Banks', 'Hostels', 'Others', 'Administrative', 'Schools')
    categories_data = dict(zip(category_ids, category_names))
    for id,name in categories_data.items():
        category = Category()
        category.category_id = id
        category.category_name = name
        db.session.add(category)
        db.session.commit()
        print(category)
    return True

@manager.command
def truncate_model(model):
    models = {'category':Category, 'location':Location}
    models[model].query.delete()




def generate_integer_string(size=10):
    """ Generate random string """
    digit = string.digits
    random_string = ''.join((random.choice(digit) for x in range(size)))
    return random_string

@manager.command
def load_location_data():
    import json
    with open('location_data.json','r') as json_data:
        locations_data = json.load(json_data)
    for location_data in locations_data:
        location_data['location_id'] = 'LOC-' + generate_integer_string(6)
        try:
            insert_location_data_into_db(location_data)
        except SQLAlchemyError:
            return False
    return True

        

def insert_location_data_into_db(location_data):
    location = Location()
    location.location_id = location_data['location_id']
    location.location_name = location_data['location_name']
    location.coordinate = "%s,%s" % (location_data['lat'], location_data['lng'])
    location.location_alias = location_data.get('location_alias')
    location.category_id = location_data['category_id']
    db.session.add(location)
    db.session.commit()




if __name__ ==  "__main__":
    manager.run()
