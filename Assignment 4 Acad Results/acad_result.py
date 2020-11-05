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

columns = ['Sem','Subject','Credits','Grade','Type']
#for roll_individual
for i,roll in enumerate(df.roll):
    name = os.path.join(path,f'{roll}_individual.csv')
    if not os.path.exists(name):
        f = open(name,'w',newline='')
        csvw = csv.writer(f)
        csvw.writerow([f"Roll: {roll}"])
        csvw.writerow([f'Semester Wise Details'])
        csvw.writerow(columns)
        f.close()
    row = list(df.values[i])
    row.pop(0)
    if row[-2] not in list(grade.keys()):
        print(f'in misc.csv {i}')
        name = os.path.join(path,'misc.csv')
        if not os.path.exists(name):
           f = open(name,'w',newline='')
           csvw = csv.writer(f)
           csvw.writerow(["Misc values"])
           csvw.writerow(columns)
           f.close() 
        with open(name,'a',newline='') as f:
            csvw = csv.writer(f)
            csvw.writerow(row)
        continue

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
           csvw.writerow(columns)
           f.close() 
        with open(name,'a',newline='') as f:
            csvw = csv.writer(f)
            csvw.writerow(row)

    

    
#for rollno_overall.csv this depends upon above code 

for file in os.listdir(path):
    if file=='misc.csv':
        continue
    data = []
    with open(os.path.join(path,file),newline='') as csvfile:
        csvr = csv.reader(csvfile,)
        skip=3
        for row in csvr:
            if skip==0:
                data.append(row)
            else:
                skip = skip -1
                if skip==0:
                    head = row

    df = pd.DataFrame(data,columns=head)
    l = (df.Sem).unique()
    total_credit = 0
    total_credit_cleared = 0
    spi_list =[]
    sem_credits_list = []
    newfile = file.split('_')[0] + '_overall.csv'
    with open(os.path.join(path,newfile),'w',newline='') as csvfile:
        csvr = csv.writer(csvfile)
        rno = file.split('_')[0]
        csvr.writerow([f'Roll: {rno}'])   
        csvr.writerow(['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI'])
        for sem in l:
            s = df[df.Sem ==sem]
            sem_credit = 0
            sem_credit = [sem_credit :=sem_credit + int(i) for i in s.Credits][-1]
            total_credit = total_credit + int(sem_credit)
            cleared_credits = 0
            for grades,credits in zip(s.Grade,s.Credits):
                if grades in list(grade.keys()) :
                    if grade[grades]>0:
                        cleared_credits = cleared_credits + int(credits)
                else:
                    print("Grade error ",grades)
                    
            total_credit_cleared = total_credit_cleared + cleared_credits
            sum_spi = 0
            for g,c in zip(s.Grade,s.Credits):
                sum_spi = sum_spi  + int(c) * int(grade[g])
            
            spi = sum_spi/sem_credit
            spi_list.append(spi)
            sem_credits_list.append(sem_credit)
            cpi_sum = 0
            for c,g in zip(sem_credits_list,spi_list):
                cpi_sum = cpi_sum + c*g
            
            cpi = cpi_sum/sum(sem_credits_list)
            csvr.writerow([sem,sem_credit,cleared_credits,round(spi,2),total_credit,total_credit_cleared,round(cpi,2)])




        
        




