from sqlalchemy.orm import Session
import models, schemas

def get_all_employees(db: Session):
    return db.query(models.Employee).all()

def get_employee_by_id(db: Session, emp_id: int):
    return (
        db
        .query(models.Employee)
        .filter(models.Employee.id == emp_id)
        .first()
    )

def create_employee(db: Session, employee_data: schemas.EmployeeCreate):
    db_employee = models.Employee(
        name= employee_data.name, email= employee_data.email
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee(db: Session, emp_id: int, employee_data: schemas.EmployeeUpdate):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db_employee.name = employee_data.name
        db_employee.email = employee_data.email
        db.commit()
        db.refresh(db_employee)
    return db_employee

def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee