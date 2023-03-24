from dataclasses import dataclass

@dataclass
class Exam:
    examID: int

    def __init__(self, examID: int):
        self.examID = examID

    def __str__(self):
        return f"{self.examID}"

@dataclass
class Patient:
    patientID: int
    name: str
    exams: set()

    def __init__(self, patID: int, name: str):
        self.patientID = patID
        self.name = name
        self.exams = set()

    def __str__(self):
        return f"Name: {self.name}, Id: {self.patientID}, Exam Count: {len(self.exams)}"

class PatientPortal:
    patientDict: {}
    examToPatientDict: {}

    def __init__(self):
        self.patientDict = {}
        self.examToPatientDict = {}



#use dataclasses
#hashmap of patient IDs to patient classes
#patient class includes a set exam classes
#exam ids to patient id hashmap
#wrap everything in a bigger class that simplify calls
#unit tests!!! with pytest
#format code with black
