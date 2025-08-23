from fastapi import FastAPI, status, HTTPException
from typing import List
from model import Employee

app = FastAPI()

employeesdb: List[Employee]  = []

@app.get("/employee", response_model= List[Employee], status_code=status.HTTP_200_OK)
def get_all_employee():
    return employeesdb

@app.get("/employee/{emp_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def get_employee_by_id(emp_id: int):
    for index, employee in enumerate(employeesdb):
        if employee.id == emp_id:
            return employeesdb[index]
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee not found with id: {emp_id}"
    )

@app.post("/employee", response_model=Employee, status_code=status.HTTP_201_CREATED)
def create_employee(employee_data: Employee):
    for index, employee in enumerate(employeesdb):
        if employee.id == employee_data.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Employee with {employee_data.id} already exits"
            )
    employeesdb.append(employee_data)
    return employee_data

@app.put("/employee/{emp_id}", response_model=Employee, status_code=status.HTTP_200_OK)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employeesdb):
        if employee.id == emp_id:
            employeesdb[index] = updated_employee
            return updated_employee
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee not found with id: {emp_id}"
    )

@app.delete("/employee/{emp_id}", status_code=status.HTTP_200_OK)
def delete_employee(emp_id: int):
    for index, employee in enumerate(employeesdb):
        if employee.id == emp_id:
            del employeesdb[index]
            return {"detail": f"Employee with id {emp_id} deleted successfully"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Employee not found with id: {emp_id}"
    )