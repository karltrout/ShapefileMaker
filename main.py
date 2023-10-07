import getopt
import sys
import pandas as pd


def readfile(file):
    filedata = pd.read_csv(file)
    print(filedata)


def main(argv):
    inputfile = ''
    opts, args = getopt.getopt(argv, "hi:", ["ifile="])
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
    print('Input file is ', inputfile)

    readfile(inputfile)


if __name__ == "__main__":
    main(sys.argv[1:])
