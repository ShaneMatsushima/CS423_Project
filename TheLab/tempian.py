#!/usr/bin/env python

'''
CS 423, Lab 5 Solution
Spring 2024
Global alignment algorithm with dynamic programming

Author: Tammy VanDeGrift
Adapted from Tammy VanDeGrift
'''

from helpers.lab5helper import createTable, printTable, convertFileToSequence, generateRandomDNA, globalAlignmentScore
from openpyxl import Workbook, load_workbook


###################################################
### Testing #######################################
###################################################

if __name__ == '__main__':
    # Calculate global alignment score of two sequences pulled from an excel file
    workbook = load_workbook(filename="excelfiles/hello.xlsx")
    sheet = workbook.active
    s = ""
    t = ""
    for i in range(1,18):
        pos = "A"+str(i)
        s = s + str(sheet[pos].value)
    for i in range(20,37):
        pos = "A"+str(i)
        t = t + str(sheet[pos].value)
    optimalScore = globalAlignmentScore(s, t)
    print(s)
    print(t)
    print("Global alignment score: " + str(optimalScore))

