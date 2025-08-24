from fastapi import FastAPI, HTTPException, status, Depends
from database import Base, engine, SessionLocal
import schemas, crud
from sqlalchemy.orm import Session
from typing import List


app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/employee", response_model=schemas.EmployeeOut, status_code=status.HTTP_201_CREATED)
def create_employee(employee_data: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    return crud.create_employee(db, employee_data)

@app.get("/employees", response_model=List[schemas.EmployeeOut], status_code=status.HTTP_200_OK)
def get_all_employee(db: Session = Depends(get_db)):
    return crud.get_all_employees(db)

@app.get("/employee/{emp_id}", response_model=schemas.EmployeeOut, status_code=status.HTTP_200_OK)
def get_employee_by_id(emp_id: int, db: Session = Depends(get_db)):
    employee = crud.get_employee_by_id(db, emp_id)
    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee not found with id: {emp_id}"
        )
    return employee

@app.put("/employee/{emp_id}", response_model=schemas.EmployeeOut, status_code=status.HTTP_200_OK)
def update_employee(emp_id: int, employee_data: schemas.EmployeeUpdate, db: Session=Depends(get_db)):
    employee = crud.update_employee(db, emp_id, employee_data)
    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee not found with id: {emp_id}"
        )
    return employee

@app.delete("/employee/{emp_id}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_employee(emp_id: int, db: Session=Depends(get_db)):
    employee = crud.delete_employee(db, emp_id)
    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee not found with id: {emp_id}"
        )
    return {
        "message": f"Employee with id: {emp_id} removed successfully."
    }
