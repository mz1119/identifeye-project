from dataclasses import dataclass, field


@dataclass(eq=True)
class Patient:
    patID: int
    name: str
    exams: set[int] = field(default_factory=set)

    def __str__(self):
        return f"Name: {self.name}, Id: {self.patID}, Exam Count: {len(self.exams)}"


class PatientPortal:
    def __init__(self):
        self.patientDict = {}
        self.examToPatientDict = {}

    def add_patient(self, patID: int, name: str):
        if patID in self.patientDict:
            return
        self.patientDict[patID] = Patient(patID, name)

    def add_exam(self, patID: int, examID: int):
        if patID not in self.patientDict:
            return
        if examID in self.examToPatientDict:
            return
        # use this dict to track examID to patID relation in case of deletion
        self.examToPatientDict[examID] = patID
        # add exam to patient class with given patID
        self.patientDict[patID].exams.add(examID)

    def delete_patient(self, patID: int):
        if patID not in self.patientDict:
            return
        del self.patientDict[patID]

    def delete_exam(self, examID: int):
        if examID not in self.examToPatientDict:
            return
        # delete exam from set in patient class
        patID = self.examToPatientDict[examID]
        self.patientDict[patID].exams.remove(examID)

    def print_record(self):
        for patient in self.patientDict.values():
            print(patient)
