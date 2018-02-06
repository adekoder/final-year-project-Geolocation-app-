from test import db,BaseAppTest
from app.models import Location, Category

class TestAppModel(BaseAppTest):

    def test_location_model(self):
        location = Location()
        location.location_id = 'LOC-123444'
        location.location_name = 'School caffietaria'
        location.coordinate = "6.544443,3.375656"
        location.category_id = '228383838'
        db.session.rollback()
        db.session.add(location)
        self.assertEqual(None, db.session.commit())

    def test_category_model(self):
        category = Category()
        category.category_id = '228383838'
        category.category_name = 'Others'
        db.session.rollback()
        db.session.add(category)
        self.assertEqual(None, db.session.commit())
        
