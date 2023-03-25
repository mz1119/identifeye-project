import sys
import os
import pytest

#importing from parent directory
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Classes import PatientPortal, Patient


def test_add_patient():
    portal = PatientPortal()

    #adding patient with same ID
    portal.add_patient(123, "John Doe")
    portal.add_patient(123, "Not John Doe")

    assert portal.patientDict[123] == Patient(123, "John Doe", set())

def test_add_exam():
    portal = PatientPortal()

    #adding exam for nonexistent patient
    portal.add_exam(123, 456)
    assert portal.patientDict == {}

    #adding exam for existing patient
    portal.add_patient(123, "John Doe")
    portal.add_exam(123, 456)

    assert portal.patientDict[123] == Patient(123, "John Doe", {456})
    assert str(portal.patientDict[123]) == "Name: John Doe, Id: 123, Exam Count: 1"

    #adding exam with same identifier to different person shouldn't do anything
    portal.add_patient(789, "Mary Jane")
    portal.add_exam(789,456)

    assert portal.patientDict[789] == Patient(789, "Mary Jane", set())
    assert str(portal.patientDict[789]) == "Name: Mary Jane, Id: 789, Exam Count: 0"

def test_delete_patient():
    portal = PatientPortal()

    #deleting nonexistent patient
    portal.delete_patient(123)
    assert portal.patientDict == {}

    #deleting existing patient
    portal.add_patient(123, "John Doe")
    assert portal.patientDict[123] == Patient(123, "John Doe", set())
    assert str(portal.patientDict[123]) == "Name: John Doe, Id: 123, Exam Count: 0"
    portal.delete_patient(123)
    assert portal.patientDict == {}

def test_delete_exam():
    portal = PatientPortal()

    #delete from empty list
    portal.delete_exam(123)
    assert portal.patientDict == {}

    portal.add_patient(123, "John Doe")
    portal.add_exam(123, 456)
    assert portal.patientDict[123] == Patient(123, "John Doe", {456})
    assert str(portal.patientDict[123]) == "Name: John Doe, Id: 123, Exam Count: 1"
    portal.delete_exam(456)
    assert portal.patientDict[123] == Patient(123, "John Doe", set())
    assert str(portal.patientDict[123]) == "Name: John Doe, Id: 123, Exam Count: 0"

