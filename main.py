''' writen by Greg Parker
    main fuction to updatetransactions
    02/16/2015
'''
import sys
from UpdateTransactions import newTransactions
import os
import string


def main(argv=None):
   cwd = os.getcwd()
   # will eventually pass this in from the command line
   oldtranslocation = cwd + '/Data/transactions_Checking_02-14-2015.csv'
   newtranslocation = cwd + '/Data/Workbook1.csv'

   nt = newTransactions('MyCheckBookTransactions')
   nt.convertToMacCSV(oldtranslocation,newtranslocation)

if __name__ == "__main__":
    sys.exit(main())
