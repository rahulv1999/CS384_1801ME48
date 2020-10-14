import csv
import os
import re


def course():
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
    with open('studentinfo_cs384.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        if not os.path.exists('country'):
            os.mkdir('country')
        for row in reader:
            l = list(row.values())
            head = list(row.keys())
            with open('country/'+row['country']+ '.csv', mode = 'a') as f:
                f_write = csv.writer(f, delimiter=',',lineterminator='\r')
                if os.path.getsize('country/'+row['country'] + '.csv')==0:
                  f_write.writerow(head) 
                f_write.writerow(l)
            f.close()
    csvfile.close()




def email_domain_extract():
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
    # Read csv and process
    pass


def state():
    # Read csv and process
    pass


def blood_group():
    # Read csv and process
    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():
    # Read csv and process
    pass

if __name__ == "__main__":
    gender()