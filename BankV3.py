# Bankv3 - Object Oriented Python Irv Kalb Listing 4-5
import pylama
from accounts import *

accountsDict ={}
nextAccountNumber = 0

oAccount = Account('Joe',100,'JoesPassword')
joesAccountNumber = nextAccountNumber
accountsDict[joesAccountNumber] = oAccount
print(f'Account number for Joe is: {joesAccountNumber}')
nextAccountNumber = nextAccountNumber+ 1

oAccount=Account('Mary',12345, 'MarysPassword')
marysAccountNumber = nextAccountNumber
accountsDict[marysAccountNumber] = oAccount
print(f'Account number for Mary is: {marysAccountNumber}')
nextAccountNumber = nextAccountNumber + 1

oAccount = Account('Bill',200,'BillsPassword')
billsAccountNumber = nextAccountNumber
accountsDict[billsAccountNumber] = oAccount
print(f'Account number for Bill is: {billsAccountNumber}')
nextAccountNumber = nextAccountNumber + 1

accountsDict[joesAccountNumber].show()
accountsDict[marysAccountNumber].show()
accountsDict[billsAccountNumber].show()
