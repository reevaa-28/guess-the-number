from fastapi import FastAPI
from pydantic import  BaseModel
from typing import List

app = FastAPI()

class Student(BaseModel):
    id:int
    name:str
    course:str

students: List[Student] = []

@app.get("/")
def read_root():
     return{"message": "Welcome to the Student Management System "}

@app.get("/students")
def get_students():
    return Student

@app.post("/add-student")
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added successfully"}

@app.put("/update-student/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, item in enumerate(students):
        if item.id == student_id:
            students[index] = updated_student
            return {"message": "Student data updated successfully"}

    return {"error": "Student not found"}