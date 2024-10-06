from config import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True) # unique identifier for the contact
    first_name = db.Column(db.String(50), unique=False, nullable=False) # first name of the contact, cannot be null
    last_name = db.Column(db.String(50), unique=False, nullable=False) # lasr name of the contact, cannot be null
    email = db.Column(db.String(100), unique=True, nullable=False) # email of the contact, cannot be null, must be unique
    
    # Converts above fields into python dictionary, which then converts to json to use to pass through API
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }
