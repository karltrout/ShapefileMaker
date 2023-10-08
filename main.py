import getopt
import re
import sys
import pandas as pd


def readfile(file):
    filedata = pd.read_csv(file)
    filedata.drop(columns=['Lower Altitude', 'Lat Lon Neighbor'], inplace=True)
    artccs = filedata.groupby("Facility ID")
    for name in artccs.groups:
        print(name)
    zny = artccs.get_group("ZNY")
    print(zny)


def dms2dd(dms: str):
    pattern = r"(\d{3})(\d{2})(\d{2})(\d{2})([N,S,E,W]{1})" if (len(dms) == 10) \
        else r"(\d{2})(\d{2})(\d{2})(\d{2})([N,S,E,W]{1})"
    results = re.fullmatch(pattern, dms)
    if results is None:
        return float('NaN')
    degrees, minutes, seconds, decisecond, direction = re.search(pattern, dms).groups()
    dd = float(degrees) + float(minutes)/60 + float(seconds)/(60*60) + float(decisecond)*.01
    if direction in ('S', 'W'):
        dd *= -1
    return dd


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
