from Classes import PatientPortal
import glob

def main():
    portal = PatientPortal()

    #finds first filename endig with .txt
    filename = glob.glob('./*.txt')[0]
    file = open(filename, 'r')

    for line in file.readlines():
        lineList = line.strip().split(" ")
        print(lineList)


if __name__ == "__main__":
    main()