from flask import request, abort
from flask_restx import Resource

from ..utils.dto import EmployeeDto
from ..services.employee_service import (get_employee_by_id,
                                         get_employees_in_organization)

from ..models.employee import Employee as EmployeeModel

api = EmployeeDto.api
_employee = EmployeeDto.employee

# TODO: add argument parsing functionality. Note that Flasks's reqparse is depricated,
# so should use marshmallow or similar instead.

@api.route("/<employee_id>",
           doc={
               "description": "Single employee.<br>"
           })
@api.response(401, "Employee not found.")
class Employee(Resource):
    @api.doc("Single employee", description="Gets a single employee by their database id (for illustrative purposes, an integer starting at 0 that increments by 1).", params={"employee_id": "The integer id assigned to the employee in the database."})
    @api.marshal_with(_employee, 200)
    def get(self, employee_id):
        lang = request.args["lang"] or "en"  # For now, default to english if no language specified.
        if get_employee_by_id(employee_id):
            return get_employee_by_id(employee_id).json(lang)
        return abort(401, "Employee not found.")

    

    
