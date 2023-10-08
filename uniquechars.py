import csv
from pandas import *
import sys
import pandas as pd
import numpy as np

# f = open('te-d1-analytics.txt', 'w')
# f = open('ted2-analytics.txt', 'w')
# f = open('ted3-analytics.txt', 'w')
# f = open('ted4-analytics.txt', 'w')
# f = open('bhd1-analytics.txt', 'w')
# f = open('bhd2-analytics.txt', 'w')
f = open('bhd3-analytics.txt', 'w')
# f= open('mtd4-analysis.txt','w')

sys.stdout = f

# fname="telugu_data_new.csv"
# fname="bhoj_data_new.csv"
# fname="mt_data_new.csv"
fname="bhoj_d3_new.csv"
data = read_csv(fname,low_memory=False)
sentences = data['Text'].tolist()
codes= data['Code'].tolist()
uniquechars=[]
extrachars=[]
# charlist=[',', '', '.', '', '?', '', 'ం', '',
#          'ః', '', 'అ', '', 'ఆ', '', 'ఇ', '', 'ఈ', '', 'ఉ', '', 'ఊ', '', 'ఋ', 
#          '', 'ఎ', '', 'ఏ', '', 'ఐ', '', 'ఒ', '', 'ఓ', '', 'ఔ', '', 'క', '', 'ఖ', 
#          '', 'గ', '', 'ఘ', '', 'చ', '', 'ఛ', '', 'జ', '', 'ఞ', '', 'ట', '', 'ఠ', '', 
#          'డ', '', 'ఢ', '', 'ణ', '', 'త', '', 'థ', '', 'ద', '', 'ధ', '', 'న', '', 
#          'ప', '', 'ఫ', '', 'బ', '', 'భ', '', 'మ', '', 'య', '', 'ర', '', 'ల', 
#          '', 'ళ', '', 'వ', '', 'శ', '', 'ష', '', 'స', '', 'హ', '', 'ా', '', 'ి',
#          '', 'ీ', '', 'ు', '', 'ూ', '', 'ృ', '', 'ె', '', 'ే', '', 'ై', '', 'ొ', '',
#          'ో', '', 'ౌ', '', '్']
# charlist=[',', '', '.', '', '?', '', 'ँ', '', 'ं', '', 'ः', '', 'अ', '', 'आ', '', 'इ', '', 'ई', '', 'उ', '', 
#           'ऊ', '', 'ऋ', '', 'ए', '', 'ऐ', '', 'ऑ', '', 'ओ', '', 'औ', '', 'क', '', 'ख', '', 'ग', '', 'घ', '', 'च', 
#           '', 'छ', '', 'ज', '', 'झ', '', 'ञ', '', 'ट', '', 'ठ', '', 'ड', '', 'ढ', '', 'ण', '', 'त', '', 'थ', '', 'द',
#           '', 'ध', '', 'न', '', 'प', '', 'फ', '', 'ब', '', 'भ', '', 'म', '', 'य', '', 'र', '', 'ल', '', 'व', '', 'श', '', 
#           'ष', '', 'स', '', 'ह', '', 'ऽ', '', 'ा', '', 'ि', '', 'ी', '', 'ु', '', 'ू', '', 'ृ', '', 'े', '', 'ै', '', 
#           'ॉ', '', 'ो', '', 'ौ', '', '्', '', 'क़', '', 'ख़', '', 'ज़', '', 'ड़', '', 'ढ़', '', 'फ़']
charset=[',', '', '.', '', '?', '', 'ँ', '', 'ं', '', 'ः', '', 'अ', '', 'आ', '', 'इ', '', 'ई', '', 'उ', '',
         'ऊ', '', 'ऋ', '', 'ए', '', 'ऐ', '', 'ऑ', '', 'ओ', '', 'औ', '', 'क', '', 'ख', '', 'ग', '', 'घ', '', 'ङ', 
         '', 'च', '', 'छ', '', 'ज', '', 'झ', '', 'ञ', '', 'ट', '', 'ठ', '', 'ड', '', 'ढ', '', 'ण', '', 'त', '', 'थ',
         '', 'द', '', 'ध', '', 'न', '', 'प', '', 'फ', '', 'ब', '', 'भ', '', 'म', '', 'य', '', 'र', '', 'ल', '', 'व', '', 
         'श', '', 'ष', '', 'स', '', 'ह', '', 'ऽ', '', 'ा', '', 'ि', '', 'ी', '', 'ु', '', 'ू', '', 'ृ', '', 'ॅ', '', 'े', 
         '', 'ै', '', 'ॉ', '', 'ो', '', 'ौ', '', '्', '', 'क़', '', 'ख़', '', 'ग़', '', 'ज़', '', 'ड़', '', 'ढ़', '', 'फ़']
charlist=set(charset)
# charlist={' ',',','.','?','ँ','ं','ः','अ','आ','इ','ई','उ','ऊ','ऋ','ए','ऐ','ऑ','ओ','औ',
#           'क','ख','ग','घ','ङ','च','छ','ज','झ','ञ','ट','ठ','ड','ढ','ण','त','थ','द','ध','न','प','फ','ब',
#           'भ','म','य','र','ल','व','श','ष','स','ह','ऽ','ा','ि','ी','ु','ू','ृ','ॅ','े','ै','ॉ','ो','ौ','्',
#           'क़','ख़','ग़','ज़','ड़','ढ़','फ़'}
onebigsentence=""
for i in range(0,len(codes)):
      # if data['Dialect'][i]=="D4":
            # print(sentences[i])
      if str(sentences[i])!='nan':
            onebigsentence=onebigsentence+sentences[i]
            for x in sentences[i]:
                  if x not in uniquechars:
                        uniquechars.append(x)
                        if x not in charlist:
                              extrachars.append(x)
unique, counts = np.unique(np.array(list(onebigsentence)), return_counts=True)
print(len(unique))
all_freq = dict(zip(unique, counts)) 
print("list of unique characters: ", unique) 
print("dict of unique character frequencies: ", all_freq)
print("list of different characters not in provided list: ", extrachars)
no_other_char=0
other_chars_present=0
if ' ' in extrachars:
      extrachars.remove(' ')
for i in range(0,len(codes)):
      # if data['Dialect'][i]=="D4":
      flag=0
      for x in extrachars:
            if str(sentences[i])!='nan':
                  if x in sentences[i]:
                        flag=1
      if flag==0:
            no_other_char=no_other_char+1
      else:
            other_chars_present=other_chars_present+1
            # print`(sentences[i])
print("no of sentences with no other chars: ", no_other_char)
print("no of sentences wit other chars present: ", other_chars_present)
print("total no of sentences: ", other_chars_present+no_other_char)
field_names= ['char','freq']
with open('bhd3.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(0,len(unique)):
      writer.writerow([unique[i],counts[i]])
      
onebigsentence=""
for i in range(0,len(codes)):
      # if data['Dialect'][i]=="D4":
      if str(sentences[i])!='nan':
      # print(sentences[i])
            onebigsentence=onebigsentence+" "+sentences[i]
list_of_words=onebigsentence.split()
unique_words=set(list_of_words)
length = len(unique_words)
print("no of unique words: ",length) 
# print(unique_words)