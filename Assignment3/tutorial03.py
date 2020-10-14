import csv
import os
import re
import shutil



def course():
    if os.path.exists('course'):
        shutil.rmtree('course')
    d = {'01':'btech',
    '11':'mtech',
    '21':'phd',
    '12':'msc'}
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('course'):
            os.mkdir('course')
        for row in reader:
            if len(row)==0:
                print(1)
                continue
            l = list(row.values())
            head = list(row.keys())
            stream = str(row['id'][-4:-2]).lower()
            yr = str(row['id'][:2])
            if str(row['id'][2:4]) in list(d.keys()):
                degree = d[str(row['id'][2:4])]
            else:
                with open('course/' + 'misc.csv' , mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('course/' + 'misc.csv')==0:
                        f_write.writerow(head)
                    f_write.writerow(l)
                f.close()
                continue
            csv_name = f'{yr}_{stream}_{degree}.csv'
            p = re.compile(r'\d\d\d\d\D\D\d\d')
            k = re.fullmatch(p,row['id'])
            if k:
                if not os.path.exists('course/'+ stream):
                    os.mkdir('course/'+ stream) 
                if not os.path.exists('course/'+ stream + '/' + degree):
                    os.mkdir('course/'+ stream + '/' + degree ) 
                with open('course/'+ stream + '/' + degree + '/' + csv_name , mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('course/'+ stream + '/' + degree + '/' + csv_name)==0:
                        f_write.writerow(head)
                    f_write.writerow(l)
                f.close()
            else:
                with open('course/' + 'misc.csv' , mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('course/' + 'misc.csv')==0:
                        f_write.writerow(head)
                    f_write.writerow(l)
                f.close()
    csvfile.close()


def country():
    if os.path.exists('country'):
        shutil.rmtree('country')    
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('country'):
            os.mkdir('country')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('country/'+row['country'].lower()+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('country/'+row['country'].lower() + '.csv')==0:
                  f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()




def email_domain_extract():
    if os.path.exists('email_domain_extract'):
        shutil.rmtree('email_domain_extract')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('email'):
            os.mkdir('email')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            if '@' in row['email'] and '.' in row['email']:
                domain = row['email'].split('@')[1].split('.')[0]
                with open('email/'+domain+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('email/'+ domain + '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
                f.close()

            else:
                with open('email/'+'misc'+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('email/'+ domain + '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
                f.close()





def gender():
    if os.path.exists('gender'):
        shutil.rmtree('gender')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('gender'):
            os.mkdir('gender')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            gender = row['gender'].lower()
            with open('gender/'+gender+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('gender/'+ gender + '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
            f.close()
    csvfile.close()


def dob():
    if os.path.exists('dob'):
        shutil.rmtree('dob')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('dob'):
            os.mkdir('dob')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            yr = int(row['dob'].split('-')[-1])
            k = int(yr)%10
            if k>4:
                name = 'bday_' + str(yr - k + 5) + '_' + str(yr - k + 9)
            else:
                name = 'bday_' + str(yr - k ) + '_' + str(yr - k + 4)
            if yr > 2014:
                name = 'bday_2015_2020'
            with open('dob/'+name+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('dob/'+name+ '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
            f.close()
        



def state():
    if os.path.exists('state'):
        shutil.rmtree('state')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('state'):
            os.mkdir('state')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('state/'+row['state'].lower()+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('state/'+row['state'].lower() + '.csv')==0:
                  f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()


def blood_group():
    if os.path.exists('blood_group'):
        shutil.rmtree('blood_group')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('blood_group'):
            os.mkdir('blood_group')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('blood_group/'+row['blood_group']+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('blood_group/'+row['blood_group'] + '.csv')==0:
                    f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()


# Create the new file here and also sort it in this function only.
def new_file_sort():
    new = []
    head = []
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)       
        for row in reader:
            head = list(row.keys())
            del head[1]
            head.insert(1,'first_name')
            head.insert(2,'last_name')
            k = list(row.values())
            del k[1]
            k.insert(1,row['full_name'].split()[0])
            k.insert(2,' '.join(row['full_name'].split()[1:]))
            new.append(k)
    csvfile.close()
    with open('studentinfo_cs384_names_split.csv', newline='') as f:
        f_write = csv.writer(f, delimiter=',',lineterminator='\r')
        f_write.writerow(head)
        for i in new:
            f_write.writerow(i)
    f.close()
    #sorting
    dic = {}
    for i in new:
        dic[i[1]]='#$%^&*'.join(i)
    new = []
    for i in sorted(dic.items()):
        new.append(i[1].split('#$%^&*'))
    with open('studentinfo_cs384_names_split_sorted_first_name.csv', mode = 'a') as f:
        f_write = csv.writer(f, delimiter=',',lineterminator='\r')
        f_write.writerow(head)
        for i in new:
            f_write.writerow(i)
    f.close()

# if __name__ == "__main__":
#     country()