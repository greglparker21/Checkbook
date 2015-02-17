''' written by Greg Parker to parse CC transations and
    add them to a running spreadsheet that keeps all my banking transactions
    each pay period
    02/16/2015
'''
import xlrd
import csv


class newTransactions():
    def __init__(self,name):
        self.name = name

    def convertToTrueCSV(self,o_location,n_location):
      fi = open(o_location, 'rb')
      data = fi.read()
      fi.close()
      fo = open(n_location, 'wb')
      fo.write(data.replace('\x00', ''))
      fo.close()

    def getNewTransactions(self,location):
        with open(location,'rb') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print row
    '''

    def parseTransactions(self):
    def updateMainSpreadSheet(self):
    '''
