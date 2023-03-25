from Classes import PatientPortal
import glob


def main():
    portal = PatientPortal()

    # finds first file ending with .txt in data directory
    filename = glob.glob("./data/*.txt")[0]
    file = open(filename, "r")

    for line in file.readlines():
        line = line.strip().split(" ")

        if line[0] == "ADD" and line[1] == "PATIENT":
            portal.add_patient(int(line[2]), " ".join(line[3:]))
        elif line[0] == "ADD" and line[1] == "EXAM":
            portal.add_exam(int(line[2]), int(line[3]))
        elif line[0] == "DEL" and line[1] == "PATIENT":
            portal.delete_patient(int(line[2]))
        elif line[0] == "DEL" and line[1] == "EXAM":
            portal.delete_exam(int(line[2]))

    portal.print_record()


if __name__ == "__main__":
    main()
