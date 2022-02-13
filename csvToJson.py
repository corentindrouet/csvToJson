#!/usr/bin/python3

import pandas
import json
import sys, getopt


def csvToJson(csvFilePath, jsonFilePath):
    datas = pandas.read_csv(csvFilePath, sep=";", encoding="utf-8")
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:
        datas.to_json(jsonFile, orient='records', force_ascii=False)

def main(argv):
    csvFile = ''
    jsonFile = ''

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["csvfile=","jsonfile="])
    except getopt.GetoptError:
        print('test.py -i <csvfile> -o <jsonfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print ('test.py -i <csvfile> -o <jsonfile>')
            sys.exit()
        elif opt in ("-i", "--csvfile"):
            csvFile = arg
        elif opt in ("-o", "--jsonfile"):
            jsonFile = arg

    csvToJson(csvFile, jsonFile)


if __name__ == "__main__":
    main(sys.argv[1:])
