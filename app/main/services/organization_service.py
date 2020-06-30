from ..models.organization import Organization

def get_organization_by_id(organization_id):
    '''
    Retreives a particular user by their user ID.

    Args:
        organization_id:
            An int that specifies the user_id.
    
    Returns:
        An instance of the User model.
    '''
    return Organization.query.filter_by(id=organization_id).first()
