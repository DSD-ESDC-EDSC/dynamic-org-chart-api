from flask import request, abort
from flask_restx import Resource

from ..utils.dto import EmployeesDto
from ..services.employee_service import get_employees_in_organization_2

api = EmployeesDto.api
_employees = EmployeesDto.employees

@api.route("/<organization_id>",
           doc={
               "description": "Employees within an organization.<br>"
           })
@api.response(401, "Organization not found.")
class EmployeesByOrganization(Resource):
    @api.doc("Multiple employees.<br>",
             description="Gets a list of employees who belong to a particular organization.",
             params={"organization_id": "The integer id assigned to the employee in the database."})
    @api.marshal_with(_employees, 200)
    def get(self, organization_id):
        lang = request.args["lang"] or "en"  # For now, default to english if no language specified.
        if get_employees_in_organization_2(organization_id, lang):
            return get_employees_in_organization_2(organization_id, lang)
        return abort(401, "Employee not found.")
