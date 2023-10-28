from flask_restful import Resource, reqparse
from models.employee import Employee as EmployeeModel
from flask import jsonify

class Employee(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('mobile', type=str, required=True)
        parser.add_argument('employee_id', type=str, required=True)
        parser.add_argument('department', type=str, required=True)
        parser.add_argument('designation', type=str, required=True)
        parser.add_argument('rank', type=str, required=True)
        args = parser.parse_args()

        response = EmployeeModel.add_single_employee(args)
        if response["error"]:
            return response
        
        employee = response["data"]
        
        return jsonify({
            "error": False,
            "data": employee
        })
    
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('employee_id', type=str, required=True)
        args = parser.parse_args()

        response =  EmployeeModel.get_single_employee(args)
        if response["error"]:
            return response
        
        employee = response["data"]
        
        return jsonify({
            "error": False,
            "data": employee
        })