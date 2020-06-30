from app.main.db import db

class Department(db.Model):
    '''
    The model for departments.
    '''
    __tablename__ = "departments"

    dept_id = db.Column(db.Integer, primary_key=True,)
    department_en = db.Column(db.Text())
    department_fr = db.Column(db.Text())
    org_chart_en = db.Column(db.Text())
    org_chart_fr = db.Column(db.Text())

    def __init__(self, department_en, department_fr, org_chart_en, org_chart_fr):
        self.department_en = department_en
        self.department_fr = department_fr
        self.org_chart_en = org_chart_en
        self.org_chart_fr = org_chart_fr

    def json(self, lang):
        '''
        Creates a JSON representation of the current instance of Department for
        a given language.
        Args:
            lang: "en" or "fr"
        Returns:
            A python dict containing the values for the department being searched.
        '''
        return {
            'dept_id': self.dept_id,
            'department_name': self.department_en if lang == "en" else self.department_fr,
            'org_chart': self.org_chart_en if lang == "en" else self.org_chart_fr,
        }
    
    def save_to_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.delete(self)
        db.session.commit()

