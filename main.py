from Classes import PatientPortal

def main():
    portal = PatientPortal()

    portal.add_patient(123, "John Doe")
    portal.add_exam(123, 456)
    portal.delete_exam(456)
    portal.delete_patient(123)


if __name__ == "__main__":
    main()