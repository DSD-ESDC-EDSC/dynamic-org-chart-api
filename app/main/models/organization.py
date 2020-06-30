from app.main.db import db

class Organization(db.Model):
    '''
    The model for organizations.
    '''
    __tablename__ = "organizations"

    org_id = db.Column(db.Integer, primary_key=True,)
    org_name_en = db.Column(db.Text())
    org_name_fr = db.Column(db.Text())
    dept_id = db.Column(db.Integer(), db.ForeignKey("departments.dept_id"))
    org_chart_path = db.Column(db.Text())    

    def __init__(self, org_name_en, org_name_fr, dept_id, org_chart_path):
        self.org_name_en = org_name_en
        self.org_name_fr = org_name_fr
        self.dept_id = dept_id
        self.org_chart_path = org_chart_path

    def json(self, lang):
        ''' Creates a JSON representation of the current instance of User. '''
        return {
            'org_id': self.org_id,
            'org_name': self.org_name_en if lang == "en" else self.org_name_fr,
            'dept_id': self.dept_id,
            'org_chart_path': self.org_chart_path,
        }
    
    def save_to_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.delete(self)
        db.session.commit()

