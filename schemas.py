from pydantic import BaseModel


# ---------- Department ----------

class DepartmentBase(BaseModel):
    name: str


class DepartmentCreate(DepartmentBase):
    pass


# ---------- Student Profile ----------

class StudentProfileBase(BaseModel):
    address: str
    phone: str


class StudentProfileCreate(StudentProfileBase):
    pass


class StudentProfileResponse(StudentProfileBase):
    id: int

    class Config:
        from_attributes = True


# ---------- Student ----------

class StudentBase(BaseModel):
    name: str
    email: str


class StudentCreate(StudentBase):
    department_id: int


class StudentUpdate(StudentBase):
    department_id: int


class StudentResponse(StudentBase):
    id: int
    profile: StudentProfileResponse | None = None

    class Config:
        from_attributes = True


# ---------- Department Response ----------

class DepartmentResponse(BaseModel):
    id: int
    name: str
    students: list[StudentResponse] = []

    class Config:
        from_attributes = True