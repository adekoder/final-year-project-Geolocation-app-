from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
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
    print('categories seeded')

@manager.command
def truncate_model(model):
    models = {'category':Category, 'location':Location}
    models[model].query.delete()





if __name__ ==  "__main__":
    manager.run()
