# -*- coding: utf-8 -*-
"""assignment1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-9-cz7AgNYNqyQBPl-yu0Mz8r7dxYkt1
"""

n=1
col=n
for r in range(0,n):
  for c in range(0,col):
    if(r+c==0  ):
      print("*",end="")
    else:
       print(" ",end="") 
  print()

n=3
col=n
for r in range(0,n):
  for c in range(0,col):
    if(r+c==1 or r-c==1 or c-r==1 or r+c==3 ):
      print("*",end="")
    else:
       print(" ",end="") 
  print()

n=5
col=n
for r in range(0,n):
  for c in range(0,col):
    if(r+c==2 or r-c==2 or c-r==2 or r+c==6 ):
      print("*",end="")
    else:
       print(" ",end="") 
  print()

n=7
col=n
for r in range(0,n):
  for c in range(0,col):
    if(r+c==3 or r-c==3 or c-r==3 or r+c==9 ):
      print("*",end="")
    else:
       print(" ",end="") 
  print()

n=9
col=n
for r in range(0,n):
  for c in range(0,col):
    if(r+c==4 or r-c==4 or c-r==4 or r+c==12 ):
      print("*",end="")
    else:
       print(" ",end="") 
  print()