import numpy as np
import pandas as pd
import os
import csv
import shutil
os.getcwd()
path = 'grades'
path = os.path.join(os.getcwd(),path)
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)
print(path)
df = pd.read_csv('acad_res_stud_grades.csv')

df = df.drop(['sl','year','timestamp'],axis=1)
grade = {'AA':10,
         'AB':9,
         'BB':8,
         'BC':7,
         'CC':6,
         'CD':5,
         'DD':4,
         'F' :0,
         'I' :0
          }



for i,roll in enumerate(df.roll):
    name = os.path.join(path,f'{roll}_individual.csv')
    if not os.path.exists(name):
        f = open(name,'w',newline='')
        csvw = csv.writer(f)
        csvw.writerow([f"Roll: {roll}"])
        csvw.writerow([f'Semester Wise Details'])
        csvw.writerow(['Sem','Subject','Credits','Grade','Type'])
        f.close()
    row = list(df.values[i])
    row.pop(0)
    try:
        with open(name,'a',newline='') as f:
            csvw = csv.writer(f)
            csvw.writerow(row)
    except:
        print(f'in misc.csv {i}')
        name = os.path.join(path,'misc.csv')
        if not os.path.exists(name):
           f = open(name,'w',newline='')
           csvw = csv.writer(f)
           csvw.writerow(["Misc values"])
           csvw.writerow(['Sem','Subject','Credits','Grade','Type'])
           f.close() 
        with open(name,'a',newline='') as f:
            csvw = csv.writer(f)
            csvw.writerow(row)

    

    
    