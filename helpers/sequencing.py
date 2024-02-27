'''
---App for Bio Informatics Research w/ Dr.Hutcheson---

Helper file to produce sequence functionality.
This is to ensure seperation from gui and functionality for easier testing.

Created: 2/12/2024
Author: Shane Matssuhima, Ian Thompson, Austen Furutani
'''
import json

#TODO write sequencing functions for raw data -> output: information of sequence

def loadDict(dictPath:str) -> dict:
    with open(dictPath, 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    ...