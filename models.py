from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))

    students = relationship(
        "Student",
        back_populates="department"
    )


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100), nullable=False)

    email = Column(
        String(100),
        unique=True
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    profile = relationship(
        "StudentProfile",
        back_populates="student",
        uselist=False,
        cascade="all, delete-orphan"
    )


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)

    address = Column(String(200))

    phone = Column(String(20))

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        unique=True
    )

    student = relationship(
        "Student",
        back_populates="profile"
    )