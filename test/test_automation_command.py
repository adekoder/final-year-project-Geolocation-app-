from test import BaseAppTest
from manage import load_location_data, seed_categories_data

class TestAutomationCommand(BaseAppTest):

    def test_load_location_data_func(self):
        result = load_location_data()
        self.assertTrue(result)
    
    def test_sead_categories_data(self):
        result = seed_categories_data()
        self.assertTrue(result)
