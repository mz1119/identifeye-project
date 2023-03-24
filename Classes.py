from dataclasses import dataclass

@dataclass
class Patient:
    patientID: int
    name: str
    exams: set()

    def __init__(self, patID: int, name: str):
        self.patID = patID
        self.name = name
        self.exams = set()

    def __str__(self):
        return f"Name: {self.name}, Id: {self.patID}, Exam Count: {len(self.exams)}"

class PatientPortal:
    patientDict: {}
    examToPatientDict: {}

    def __init__(self):
        self.patientDict = {}
        self.examToPatientDict = {}


    def add_patient(self, patID: int, name: str):
        #if patient with given identifier exists, move on
        if patID in self.patientDict: return
        #otherwise add to dict
        self.patientDict[patID] = Patient(patID, name)

    def add_exam(self, patID: int, examID: int):
        #if patient doesn't exist, move on
        if patID not in self.patientDict: return
        # if exam already exists, move on
        if examID in self.examToPatientDict: return
        #use this dict to track examID to patID relation in case of deletion
        self.examToPatientDict[examID] = patID
        #add exam to patient class with given patID
        self.patientDict[patID].exams.add(examID)

    def delete_patient(self, patID: int):
        # if patient doesn't exist, move on
        if patID not in self.patientDict: return
        #otherwise, delete patient
        del self.patientDict[patID]

    def delete_exam(self, examID: int):
        #if exam doesn't exist, move on
        if examID not in self.examToPatientDict: return
        #otherwise delete exam from set in patient class
        patID = self.examToPatientDict[examID]
        self.patientDict[patID].exams.remove(examID)

    def output_record(self):
        for patient in self.patientDict.values():
            print(patient)

#unit tests!!! with pytest
#format code with black
