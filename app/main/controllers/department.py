from flask import request
from flask_restx import Resource

from ..utils.dto import DepartmentDto
from ..services.department_service import get_department_org_chart

api = DepartmentDto.api
_department = DepartmentDto.department

@api.route("",
           doc={
               "description": "Get the org chart for a particular department.<br>",
           })

@api.route("/<dept_id>",
           doc={
               "description": "Department's org chart.<br>"
           })
@api.response(401, "Department not found.")
class Department(Resource):
    @api.doc("Single department", description="Gets a single department's org chart by its dept_id.", params={"dept_id": "The integer id assigned to the department in the database."})
    @api.marshal_with(_department, 200)
    def get(self, dept_id):
        lang = request.args["lang"] or "en"  # For now, default to english if no language specified.
        if get_department_org_chart(dept_id):
            return get_department_org_chart(dept_id).json(lang)
        return abort(401, "Department not found.")
