from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import (
    Department,
    Student,
    StudentProfile
)
from schemas import *
app = FastAPI()
Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/departments")
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    db_department = Department(
        name=department.name
    )
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department
@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    db_student = Student(
        name=student.name,
        email=student.email,
        department_id=student.department_id
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
@app.post("/students/{student_id}/profile")
def create_profile(
    student_id: int,
    profile: StudentProfileCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    db_profile = StudentProfile(
        address=profile.address,
        phone=profile.phone,
        student_id=student_id
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    return student
@app.get(
    "/departments/{department_id}",
    response_model=DepartmentResponse
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(
        Department.id == department_id
    ).first()
    if not department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )
    return department
@app.put("/students/{student_id}")
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    db_student.name = student.name
    db_student.email = student.email
    db_student.department_id = student.department_id
    db.commit()
    db.refresh(db_student)
    return {
        "message": "Student updated successfully",
        "student": db_student
    }
@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(
        Student.id == student_id
    ).first()
    if not db_student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
    db.delete(db_student)
    db.commit()
    return {
        "message": "Student deleted successfully"
    }
@app.delete("/departments/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):

    db_department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    if not db_department:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    db.delete(db_department)
    db.commit()

    return {
        "message": "Department deleted successfully"
    }