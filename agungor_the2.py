# -*- coding: utf-8 -*-
"""agungor_the2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZgTXUix6jstRrL2YGv7XnaVWbxpzBDrj
"""

totalnames=input('Please enter usernames and passwords: ')
totalmodifications=input('Please enter last modification information: ')
splitnames=totalnames.split(';')
splitmodifications=totalmodifications.split(';')
datalength=len(splitnames)
username=input('Please enter the username: ')
m=0
for a in range(datalength): 
  searched=splitnames[a]
  splitsearched=searched.split(':')
  if username == splitsearched[0]:
    break
  else:
    m+=1
if m==datalength:
  print('Wrong username')
else:
  password=input('Please enter the password: ')
  passwordlength=len(password)
  reversed=''
  for n in range(1,passwordlength+1):
    reversed+=password[-n]
  scrambled=splitsearched[1] 
  scrambledreverse=''
  for k in range(1,passwordlength+1):
    scrambledreverse+=scrambled[k]
  if scrambledreverse==reversed:
    for b in range(datalength):
      searcheddate=splitmodifications[b]
      splitsearcheddate=searcheddate.split(':')
      if splitsearcheddate[0]==username:
        splitdate=splitsearcheddate[1]
        indexyearmonth=splitdate.index('y')
        indexmonth=splitdate.index('m')
        lengthmonth=indexmonth-(8+indexyearmonth)
        yearstring=''
        for g in range(indexyearmonth):
          yearstring+=splitdate[g]
        yearmonth=int(yearstring)*12
        monthstring=''
        for h in range(8+indexyearmonth, indexmonth):
          monthstring+=splitdate[h]
        month=int(monthstring)
        totalmonth=yearmonth+month
        if totalmonth<6:
          print('Successful login')
        else:
          newpassword=input('Please enter your new password: ')
          newpasswordlength=len(newpassword)
          newpasswordreverse=''
          for l in range (1,newpasswordlength+1):
            newpasswordreverse+=newpassword[-l]
          ultimatepassword=scrambled.replace(reversed,newpasswordreverse,1)
          finalnames=totalnames.replace(scrambled,ultimatepassword)
          lastdate=username+':0year(s) 0month(s)'
          finaldates=totalmodifications.replace(searcheddate,lastdate)
          print(finalnames)
          print(finaldates)
  else:
      print('Wrong password')