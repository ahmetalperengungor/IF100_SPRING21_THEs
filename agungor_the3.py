# -*- coding: utf-8 -*-
"""agungor_the3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/145JXZ7xGwErmPSb07FCEj7a7eNve3PH7
"""

db=input('Please enter your purchase history: ')
splitdb=db.split(';')
#splitdb is a list containing coins and amounts for ex ['ETR:0.2', 'MAN:1.2', 'STH:-14.3']
lengthdb=len(splitdb)

coinlist=[]
amountlist=[]

for a in range(lengthdb):
  coinAndAmount=splitdb[a]
#coinAndAmount is a string showing coin and its amount for ex 'ETR:0.2' 
  splitcoinAndAmount=coinAndAmount.split(':')
#splitcoindAndAmount is a list containing 2 items which first is the coin and second one is the amount for ex ['ETR', '0.2']
  coin=splitcoinAndAmount[0]
  amountchr=splitcoinAndAmount[1]
  amount=float(amountchr)
#coin is ETR and amount is 0.2
  if coin not in coinlist:
    if amount>0:
      coinlist.append(coin)
      amountlist.append(amount)
      print(amount, coin, 'bought')
    else:
      print('You don\'t have', coin)
  else:
    coindex=coinlist.index(coin)
    specificamount=amountlist[coindex]
    specificamount+=amount
    if amount<0:
      if specificamount<0:
        print('Not enough', coin)
        specificamount-=amount
      else:
        amountlist[coindex]=specificamount
        abvalueamount=0-amount
        print(abvalueamount, coin, 'sold')
    else:
      amountlist[coindex]=specificamount
      print(amount, coin, 'bought')
#now first input has been completed
#there are 2 lists coinlist and amountlist where they have matching indexes 

wanted=input('Please enter the currency type: ')
pricedb=input('Please enter prices: ')
splitpricedb=pricedb.split(';')
#splitpricedb is a list containing 2 types of coins and their rate for ex ['EPA_SUC:0.25', EPA_TRK:0.33]
lengthsplitpricedb=len(splitpricedb)

stonks=0

for c in range(lengthsplitpricedb):
  coinAndRatio=splitpricedb[c]
#coinratio is a string which has 2 coin types and their ratio for ex EPA_SUC:0.25
  splitcoinAndRatio=coinAndRatio.split(':')
#splitcoinratio is a list containing 2 items, leftcoin_rightcoin and ratio
  temptwocoin=splitcoinAndRatio[0]
  nextsplitcoinAndRatio=temptwocoin.split('_')
#nextsplitcoinAndRatio is a list containing 2 items, leftcoin and rightcoin
  ratiostr=splitcoinAndRatio[1]
  ratio=float(ratiostr)
  leftcoin=nextsplitcoinAndRatio[0]
  rightcoin=nextsplitcoinAndRatio[1]
#ratio, leftcoin and rightcoin are main string items
  if leftcoin==wanted:
    if rightcoin in coinlist:
      nextcoindex=coinlist.index(rightcoin)
      nextspecificamount=amountlist[nextcoindex]
      stonks+=nextspecificamount/ratio
  if rightcoin==wanted:
    if leftcoin in coinlist:
      nextnextcoindex=coinlist.index(leftcoin)
      nextnextspecificamount=amountlist[nextnextcoindex]
      stonks+=nextnextspecificamount*ratio

print('You have ', format(stonks, '.2f'), ' ', wanted, '(s).', sep='')

#Ahmet Alperen Gungor 28847