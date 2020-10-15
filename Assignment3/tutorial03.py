import csv
import os
import re
import shutil

def del_create_analytics_folder():
    # del the analytics folder including subfolder
    # mkdir the analytics folder (only mkdir)
    if os.path.exists('analytics'):
        shutil.rmtree('analytics')
    if not os.path.exists('analytics'):
        os.mkdir('analytics')

def course():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
    if os.path.exists('analytics/course'):
        shutil.rmtree('analytics/course')
    d = {'01':'btech',
    '11':'mtech',
    '21':'phd',
    '12':'msc'}
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/course'):
            os.mkdir('analytics/course')
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
                with open('analytics/course/' + 'misc.csv' , mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/course/' + 'misc.csv')==0:
                        f_write.writerow(head)
                    f_write.writerow(l)
                f.close()
                continue
            csv_name = f'{yr}_{stream}_{degree}.csv'
            p = re.compile(r'\d\d\d\d\D\D\d\d')
            k = re.fullmatch(p,row['id'])
            if k:
                if not os.path.exists('analytics/course/'+ stream):
                    os.mkdir('analytics/course/'+ stream) 
                if not os.path.exists('analytics/course/'+ stream + '/' + degree):
                    os.mkdir('analytics/course/'+ stream + '/' + degree ) 
                with open('analytics/course/'+ stream + '/' + degree + '/' + csv_name , mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/course/'+ stream + '/' + degree + '/' + csv_name)==0:
                        f_write.writerow(head)
                    f_write.writerow(l)
                f.close()
            else:
                with open('analytics/course/' + 'misc.csv' , mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/course/' + 'misc.csv')==0:
                        f_write.writerow(head)
                    f_write.writerow(l)
                f.close()
    csvfile.close()


def country():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')    
    if os.path.exists('analytics/country'):
        shutil.rmtree('analytics/country')    
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/country'):
            os.mkdir('analytics/country')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('analytics/country/'+row['country'].lower()+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('analytics/country/'+row['country'].lower() + '.csv')==0:
                  f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()




def email_domain_extract():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
    if os.path.exists('analytics/email'):
        shutil.rmtree('analytics/email')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/email'):
            os.mkdir('analytics/email')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            if '@' in row['email'] and '.' in row['email']:
                domain = row['email'].split('@')[1].split('.')[0]
                with open('analytics/email/'+domain+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/email/'+ domain + '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
                f.close()

            else:
                with open('analytics/email/'+'misc'+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/email/'+ domain + '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
                f.close()
    csvfile.close()





def gender():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
    if os.path.exists('analytics/gender'):
        shutil.rmtree('analytics/gender')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/gender'):
            os.mkdir('analytics/gender')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            gender = row['gender'].lower()
            with open('analytics/gender/'+gender+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/gender/'+ gender + '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
            f.close()
    csvfile.close()


def dob():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
    if os.path.exists('analytics/dob'):
        shutil.rmtree('analytics/dob')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/dob'):
            os.mkdir('analytics/dob')
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
            with open('analytics/dob/'+name+ '.csv', mode = 'a') as f:
                    f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                    if os.path.getsize('analytics/dob/'+name+ '.csv')==0:
                        f_write.writerow(head) 
                    f_write.writerow(l)
            f.close()
        



def state():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
    if os.path.exists('analytics/state'):
        shutil.rmtree('analytics/state')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/state'):
            os.mkdir('analytics/state')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('analytics/state/'+row['state'].lower()+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('analytics/state/'+row['state'].lower() + '.csv')==0:
                  f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()


def blood_group():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
    if os.path.exists('analytics/blood_group'):
        shutil.rmtree('analytics/blood_group')
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('analytics/blood_group'):
            os.mkdir('analytics/blood_group')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('analytics/blood_group/'+row['blood_group']+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('analytics/blood_group/'+row['blood_group'] + '.csv')==0:
                    f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()


# Create the new file here and also sort it in this function only.
def new_file_sort():
    if not os.path.exists('analytics'):
        os.mkdir('analytics')
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
    with open('analytics/studentinfo_cs384_names_split.csv', newline='',mode='w') as f:
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
    with open('analytics/studentinfo_cs384_names_split_sorted_first_name.csv', mode = 'w') as f:
        print
    f.close()
    for i in sorted(dic.items()):
        new.append(i[1].split('#$%^&*'))
    with open('analytics/studentinfo_cs384_names_split_sorted_first_name.csv', mode = 'a') as f:
        f_write = csv.writer(f, delimiter=',',lineterminator='\r')
        f_write.writerow(head)
        for i in new:
            f_write.writerow(i)
    f.close()

# if __name__ == "__main__":
#     del_create_analytics_folder()
#     course()
#     blood_group()
#     new_file_sort()
#     state()
#     email_domain_extract()
#     state()
#     gender()
#     dob()
