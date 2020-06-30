from ..models.department import Department

def get_department_org_chart(dept_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        dept_id:
            An int that specifies the user_id.
    
    Returns:
        An instance of the User model.
    '''
    return Department.query.filter_by(dept_id=dept_id).first()

def get_department_list(lang):
    '''
    Returns all names and IDs for departments.
    '''
    return [item.json(lang) for item in Department.query.all()]