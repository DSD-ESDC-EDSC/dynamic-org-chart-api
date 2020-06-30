from app.main.db import db

from ..models.employee import Employee
from ..models.organization import Organization
from ..models.department import Department


def get_employee_by_id(employee_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        employee_id:
            An int that specifies the employee_id.

    Returns:
        An instance of the User model.
    '''
    return Employee.query.filter_by(employee_id=employee_id).first()

def get_employees_in_organization(organization_id, lang="en"):
    ''' Gets all employees who belong to a particular organizational unit. '''
    return [employee.json(lang) for employee in Employee.query.filter_by(org_id=organization_id)]

def get_employees_in_organization_2(organization_id, lang="en"):
    temp = [(employee.json(lang), organization.json(lang))
            for employee, organization in db.session
            .query(Employee, Organization)
            .join(Organization)
            .filter_by(org_id=organization_id)
            .join(Department)
            .all()]
    results = []
    for employee, org in temp:
        results.append({**employee, **org})
    # print("results are ", results)
    return results