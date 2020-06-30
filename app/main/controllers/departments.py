from flask import request
from flask_restx import Resource

from ..utils.dto import DepartmentsDto
from ..services.department_service import get_department_list

api = DepartmentsDto.api
_department_list = DepartmentsDto.department_list

@api.route("",
           doc={
               "description": "List of department names and IDs.<br>"
           })
@api.response(401, "Not found.")
class Departments(Resource):
    @api.doc("List of departments.", description="Gets a list of department names and IDs.")
    @api.marshal_with(_department_list, 200)
    def get(self):
        lang = request.args["lang"] or "en"  # For now, default to english if no language specified.
        if get_department_list(lang):
            return get_department_list(lang)
        return abort(401, "Not found.")
