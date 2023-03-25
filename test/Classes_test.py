import sys
import os
import pytest

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Classes import PatientPortal


def test1():
    portal = PatientPortal()

    #adding patient with same ID
    portal.add_patient(123, "John Doe")
    portal.add_patient(123, "Not John Doe")

    assert str(portal.patientDict[123]) == "Name: John Doe, Id: 123, Exam Count: 0"

