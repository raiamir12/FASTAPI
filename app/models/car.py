
from ..factories.validator import Validator
from ..factories.database import Database



class Car(object):
    
    def __init__(self):
        self.validator = Validator()
        self.db = Database()
        self.collection_name = 'cars'  # collection name

        self.fields = {
            "brand": "string",
            "model": "string",
            "year": "int",
	        "name": "string",
	        "description": "string",
	        "price": "int"
        }

        self.create_required_fields = ["name", "brand","model"]

        # Fields optional for CREATE
        self.create_optional_fields = ["year","description","price"]

        # Fields required for UPDATE
        self.update_required_fields = ["name", "brand","model"]

        # Fields optional for UPDATE
        self.update_optional_fields = ["year","description","price"]

    def create(self, car):
        # Validator will throw error if invalid
        
        self.validator.validate(car, self.fields, self.create_required_fields, self.create_optional_fields)
        res = self.db.insert(car, self.collection_name)
        return "Inserted Id " + res 
    
    def find(self, todo):  # find all
        return self.db.find(todo, self.collection_name)

    def find_by_id(self, id):
        return self.db.find_by_id(id, self.collection_name)

    def update(self, id, car):
        self.validator.validate(car, self.fields, self.update_required_fields, self.update_optional_fields)
        return self.db.update(id, car,self.collection_name)

    def delete(self, id):
        return self.db.delete(id, self.collection_name)       