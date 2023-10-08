# read the 3rd column of the input file
# check if the input characters are in between 0C00 and 0C7F

# importing module
from pandas import *
import csv

# reading CSV file
# data = read_csv("text_te - D1.csv")

# # converting column data to list
# sentences = data['SENT'].tolist()
# # for sentence in sentences:
# ch=0
# words=0
# for x in sentences[0]:
#       print(x)
#       if(x!=" "):
#             ch=ch +1;
#       else:
#             words=words+1
# # printing list data
# print(sentences[0])
# print(ch)
# print(words)
# a=hex(0x0c00)
# b=hex(0x0c7f)

#for sentence in sentences:
# newsentence= ""
# for letter in sentences[0]:
#       h= ord(letter)
#       #print(type(h))
#       #print(h)
#       if (hex(h)<a or hex(h)>b):
#             print(h)
#             print(chr(h))
#             continue
#       newsentence= newsentence + chr(h)
# print(newsentence)

# ag=0
# f=0
# corpus_codes=data['CODE'].tolist()    
# for code in corpus_codes:
#       l=code.split("_")
#       if len(l)<3:
#             continue
#       #print(l)
#       cat=l[2]
#       if cat=="AG":
#             ag= ag+1
#       elif cat=="F":
#             f= f+1
# print(ag)
# print(f)

with open("telugu_data.csv",'w') as file:
      writer=csv.writer(file)
      writer.writerow(["Code","Text","Language","Dialect","No. of char","No. of words","Category"])
      for j in {1,2,3,4}:
            fname="text_te - D"+str(j)+".csv"
            data = read_csv(fname)
            sentences = data['SENT'].tolist()
            codes= data['CODE'].tolist()
            for i in range(0,len(codes)):
                  l=codes[i].split("_")
                  if len(l)<3:
                        continue
                  cat=l[-2]
                  if cat=="AG":
                        cat="Agriculture"
                  elif cat=="F":
                        cat="Finance"
                  ch=0
                  words=0
                  if sentences[i]=="A sentence unrelated to the topic" or sentences[i]=="Repeated sentence":
                        continue
                  for x in sentences[i]:
                        if(x!=" "):
                              ch=ch +1;
                        else:
                              words=words+1
                  writer.writerow([codes[i],sentences[i],"Telugu","D"+str(j),ch,words,cat])
      file.close()
# import sys
# import math
# import pandas as pd
# import numpy as np
# # f = open('out.txt', 'w')
# # sys.stdout = f
               
# with open("bhoj_data.csv",'w') as file:
#       writer=csv.writer(file)
#       for j in {1,2,3}:
#             fname="text_bh - D"+str(j)+".csv"
#             # print(fname)
#             # #removing nan values
#             # df = pd.read_csv(fname)
#             # print("df opened")
#             # df.fillna("not available")
#             # print("df filled")
#             # df.to_csv(fname)
#             data = read_csv(fname)
#             sentences = data['SENT'].tolist()
#             codes= data['CODE'].tolist()
#             writer.writerow(["Code","Text","Language","Dialect","No. of char","No. of words","Category"])
#             for i in range(0,len(codes)):
#                   # print(codes[i])
#                   # print(sentences[i])
#                   # if str(sentences[i])=='nan':
#                   #       # sentences[i]="not available"
#                   #       print(i, "not available ")
#                   l=codes[i].split("_")
#                   if len(l)<3:
#                         continue
#                   cat=l[2]
#                   if cat=="AG":
#                         cat="Agriculture"
#                   elif cat=="F":
#                         cat="Finance"
#                   ch=0
#                   words=0
#                   if str(sentences[i])!='nan':
#                         for x in sentences[i]:
#                               # print(i)
#                               if(x!=" "):
#                                     ch=ch +1;
#                               else:
#                                     words=words+1
#                   writer.writerow([codes[i],sentences[i],"Bhojpuri","D"+str(j),ch,words,cat])
#       file.close()
      
# with open("mt_data.csv",'w') as file:
#       writer=csv.writer(file)
#       for j in {1,2,3,4}:
#             fname="text_mt - D"+str(j)+".csv"
#             data = read_csv(fname)
#             sentences = data['SENT'].tolist()
#             codes= data['CODE'].tolist()
#             writer.writerow(["Code","Text","Language","Dialect","No. of char","No. of words","Category"])
#             for i in range(0,len(codes)):
#                   l=codes[i].split("_")
#                   if len(l)<3:
#                         continue
#                   cat=l[2]
#                   if cat=="AG":
#                         cat="Agriculture"
#                   elif cat=="F":
#                         cat="Finance"
#                   ch=0
#                   words=0
#                   for x in sentences[i]:
#                         if(x!=" "):
#                               ch=ch +1;
#                         else:
#                               words=words+1
#                   writer.writerow([codes[i],sentences[i],"Maithili","D"+str(j),ch,words,cat])
#       file.close()