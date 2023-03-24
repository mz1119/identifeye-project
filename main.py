from Classes import PatientPortal

def main():
    portal = PatientPortal()

    portal.add_patient(123, "John Doe")
    portal.output_record()
    portal.add_exam(123, 456)
    portal.output_record()
    portal.delete_exam(456)
    portal.output_record()
    portal.delete_patient(123)
    portal.output_record()


if __name__ == "__main__":
    main()