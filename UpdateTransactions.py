''' written by Greg Parker to parse CC transations and
    add them to a running spreadsheet that keeps all my banking transactions
    each pay period
    02/16/2015
'''
# import Namespaces
import sys
import xlrd
import string

class newTransactions():
    def __init__(self,name):
      self.name = name

    def convertToMacCSV(self,o_location,n_location):

      fi = open(o_location, 'rb')
      data = fi.read()
      fi.close()
      fo = open(n_location, 'wb')
      readable = data.rstrip("\n").decode("utf-16")
      fo.write(readable)
      fo.close()

    def getNewTransactions(self,location):
        fi = open(location,'rb')
        i=0
        values_dict = {}
        for row in fi:
           i+=1
           row = string.replace(row,' ','')
           row = string.replace(row,'"','')
           row = string.replace(row,"'",'"')
           row = string.replace(row,'-','')
           row = string.replace(row,'\r\n','')
           if i>1:
              values=string.split(row,',')
              values_dict.setdefault('Payee', []).append(values[0])
              values_dict.setdefault('Date', []).append(values[1])
              values_dict.setdefault('Amount', []).append(float(values[2]))
        self.transactions = values_dict
        fi.close()

    def updateMainSpreadSheet(self):


