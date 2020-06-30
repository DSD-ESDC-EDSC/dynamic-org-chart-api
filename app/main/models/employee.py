from app.main.db import db

class Employee(db.Model):
    '''
    The employee model for illustrative purposes.
    '''
    __tablename__ = "employees"

    employee_id = db.Column(db.Integer, primary_key=True,)
    first_name = db.Column(db.Text(), nullable=False,)
    last_name = db.Column(db.Text(), nullable=False,)
    job_title_en = db.Column(db.Text())
    job_title_fr = db.Column(db.Text())
    phone_number = db.Column(db.Text())
    email = db.Column(db.Text())
    address_en = db.Column(db.Text())
    address_fr = db.Column(db.Text())
    province_en = db.Column(db.Text())
    province_fr = db.Column(db.Text())
    city_en = db.Column(db.Text())
    city_fr = db.Column(db.Text())
    postal_code = db.Column(db.Text())
    org_id = db.Column(db.Integer(), db.ForeignKey("organizations.org_id"))
    dept_id = db.Column(db.Integer(), db.ForeignKey("departments.dept_id"))

    def __init__(self, first_name, last_name, job_title_en, job_title_fr,
                 phone_number, email, address_en, address_fr, province_en,
                 province_fr, city_en, city_fr, postal_code, org_id, dept_id):
        self.first_name = first_name
        self.last_name = last_name
        self.job_title_en = job_title_en
        self.job_title_fr = job_title_fr
        self.phone_number = phone_number
        self.email = email
        self.address_en = address_en
        self.address_fr = address_fr
        self.province_en = province_en
        self.province_fr = province_fr
        self.city_en = city_en
        self.city_fr = city_fr
        self.postal_code = postal_code
        self.org_id = org_id
        self.dept_id = dept_id

    def json(self, lang):
        '''
        Creates a JSON representation of the current instance of User.
        Args:
            lang: "en" or "fr".
        Returns:
            A python dict with employee information.
        '''
        return {
            'employee_id': self.employee_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'job_title': self.job_title_en if lang == "en" else self.job_title_fr,
            'phone_number': self.phone_number,
            'email': self.email,
            'address': self.address_en if lang == "en" else self.address_fr,
            'province': self.province_en if lang == "en" else self.province_fr,
            'city': self.city_en if lang == "en" else self.city_fr,
            'postal_code': self.postal_code,
            'org_id': self.org_id,
            'dept_id': self.dept_id,
        }
    
    def save_to_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        ''' Saves the instance of UserModel to the database. '''
        db.session.delete(self)
        db.session.commit()

