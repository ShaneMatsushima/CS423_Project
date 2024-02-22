
# lab 5 helper functions

import random

##################################################################
# createTable
# Create a 2D table with the given number of rows and columns
# and fills all entries with value given as a parameter
# (function completed for you)
##################################################################
def createTable(nRows, nCols, value):
    return [ [value]*nCols for _ in range(nRows)]

##################################################################
# printTable
# Print 2D table to file (only useful for small tables for short
# strings)
# Should have tabs between the values on each row
# Useful function for debugging purposes
# (function completed for you)
##################################################################
def printTable(table, filename):
    with open(filename, 'w') as file:
        file.write("Table entries:\n")
        for r in table:
            for c in r:
                file.write(str(c)+"\t")
            file.write("\n")


#######################################################
# convertFileToSequence - takes a FASTA file and returns the
# DNA sequence as a string
#######################################################
def convertFileToSequence(filename):
    clean = -1
    with open(filename, 'r') as file:
        # read in first line
        header = file.readline()
        if (header[0] == '>'):
            print("in FASTA format")
            clean = 1
            # read rest of file
            sequence = file.read()
            # remove all return and newline characters
            sequence = sequence.replace("\r", "")
            sequence = sequence.replace("\n", "")
        else:
            print("invalid format")
    if(clean == -1):
         return -1  # so other functions can check
    return sequence





##################################################################
# globalAlignmentScore
# Determine the score of the optimal global alignment of two strings
# students: complete this function
##################################################################
def globalAlignmentScore(s1, s2):
    # Scoring system
    MATCH = 5
    MISMATCH = -4
    GAP = -6

    # set table size
    NUM_ROWS = len(s2)+1
    NUM_COLS = len(s1)+1

    # Create table and fill it with zeros
    costs = createTable(NUM_ROWS, NUM_COLS, 0)

    # Create table for getting back the optimal alignment, fill table with "A"
    # Suggest you use "D", "L", and "T" for diagonal, left, and top
    directions = createTable(NUM_ROWS, NUM_COLS, "A")

    # complete this part of the function
    # implement dynamic programming algorithm for global alignment here
    # fill in entries in costs table and directions table
    for i in range(1, NUM_ROWS):
         costs[i][0] = GAP * i
    for j in range(1, NUM_COLS):
         costs[0][j] = GAP * j
    for i in range(1, NUM_ROWS):
         for j in range(1, NUM_COLS):
              if (s1[j-1] == s2[i-1]):
                    lst = [costs[i][j-1] + GAP, costs[i-1][j] + GAP, costs[i-1][j-1] + MATCH]
              else:
                    lst = [costs[i][j-1] + GAP, costs[i-1][j] + GAP, costs[i-1][j-1] + MISMATCH]
               
              costs[i][j] = max(lst)
              match lst.index(max(lst)):
                   case 0: directions[i][j] = 'L'
                   case 1: directions[i][j] = 'T'
                   case 2: directions[i][j] = 'D'


    # find optimal alignment
    align(directions, s1, s2, "alignment_files\\alignment.txt")

    # return optimal score (lower right-hand cell in table]
    return costs[NUM_ROWS-1][NUM_COLS-1]


################################################################
# Reconstruct the optimal alignment and print the alignment
# to a file. Because the sequences can be long, print the
# alignment 50 characters on one line, the other string of 50 characters
# on the next line, and then skip one line, as follows:
# AATT--GGCTATGCT--C-G-TTACGCA-TTACT-AA-TCCGGTC-AGGC
# AAATATGG---TGCTGGCTGCTT---CAGTTA-TGAACTCC---CCAGGC
#
# TATGGGTGCTATGCTCG--T--TACG-CA
# TCAT--TGG---TGCTGGCTGCTT--ACA
#
# Students: Complete this function
# direction is a 2D table, seq1 and seq2 are the original DNA
# sequences to align, and filename is the name of the output file
###############################################################
def align(direction, s1, s2, filename):
     numRows = len(direction)
     numCols = len(direction[0])
     # complete this function - find optimal alignment
     backwardsSeq1 = ""
     backwardsSeq2 = ""
     curRow=numRows-1
     curCol=numCols-1
     dir = direction[curRow][curCol]
     while dir != "A":
          if dir == "T":
              backwardsSeq1 = backwardsSeq1 + "-"
              backwardsSeq2 = backwardsSeq2 + s2[curRow-1]
              curRow = curRow-1
          elif dir == "L":
              backwardsSeq1 = backwardsSeq1 + s1[curCol-1]
              backwardsSeq2 = backwardsSeq2 + "-"
              curCol = curCol-1
          else:
              backwardsSeq1 = backwardsSeq1 + s1[curCol-1]
              backwardsSeq2 = backwardsSeq2 + s2[curRow-1]
              curRow=curRow-1
              curCol=curCol-1
          dir = direction[curRow][curCol]
             
     alignedSeq1 = backwardsSeq1[::-1]
     alignedSeq2 = backwardsSeq2[::-1]

     # print alignment to output file, 50 characters per line
     with open(filename, 'w') as file:
          file.write("Alignment:\n")
          counter = 0
          while(counter < len(alignedSeq1)):
               file.write(alignedSeq1[counter:counter+50])
               file.write("\n")
               file.write(alignedSeq2[counter:counter+50])
               file.write("\n\n")
               counter = counter+50

     return

########### End of functions ###################################