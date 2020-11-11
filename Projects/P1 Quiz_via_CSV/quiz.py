import sqlite3
import hashlib, binascii, os
import  time
import pandas as pd
from pynput import keyboard
import threading


conn = sqlite3.connect('project1 quiz cs384.db')
c = conn.cursor()

def time_dis(t,roll_no,name):
    while t+1: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        os.system(f"title {roll_no}          {name.upper()}         {timer}") 
        time.sleep(1) 
        t -= 1
    
def question():
    for q in q_list:
        ans[q] = dis_q(q)

def dis_q(q_no):
    
    if q_no < len(df):
       
        print(f'Q{q_no + 1})', df.question[q_no],'\n',\
            'option1)',df.option1[q_no],'\n','option2)',df.option2[q_no],'\n',\
                'option3)',df.option3[q_no],'\n',\
            'option4)',df.option4[q_no],'\n')
        while True:
            x = input("Enter your choice 1,2,3,4,S(skip): ")
            try:
                x = int(x)
                if x in range(1,5):
                    q_list.pop(q_no)
                    break
                else:
                    print("invalid choice enter again")
            except:
                if x.lower() == 's':
                    question()
                else:
                    print("invalid choice enter again")
        return x
    else:
        print(f"there are only {len(df)} questions. choose accordingly..")


def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


try:
    c.execute("""CREATE TABLE  project1_registration (
                            roll text,
                            pass text,
                            name_stud text,
                            whatsapp_no number,

                                        )""")
    c.execute("""CREATE TABLE  project1_marks (
                            roll text,
                            quiz_num password,
                            total_marks number
                                        )""")
    conn.commit()
except :
    print


def unattempted_q():
    print(f'there are {len(q_list)} unattempted question(s) ')

def goto():
    while True:
        try:
            q_no = int(input("enter the question numer : "))
        except:
            print("invalid input..")

    ans[q_no] = dis_q(q_no)

def total_marks():
    marks = 0
    for i in len(df):
        if i in list(ans.keys()):
            if int(ans[i]) == int(df.correct_option[i]):
                marks += int(df.marks_correct_ans[i])
            else:
                marks += int(df.marks_wrong_ans[i])
        else:
            if df.compulsory[i] == 'y':
                 marks += int(df.marks_wrong_ans[i])
    return marks


def stats():
    print("Total Quiz Questions:",len(df))
    print("Total Quiz Questions Attempted:",len(quiz_list))
    print("Total Correct Question:",)
    print("Total Wrong Questions:",)
    print("Total Marks: obtained marks/total marks",total_marks())

def final_submit():
    while True:
        option =  input(' Do you want to final submit? (y/n) ')
        if option.lower() == 'y':
            print("Submitted Thankyou ...")
            submit()
            stats()
            print("press Ctrl+Alt+E to export data to csv")
            print("press any key to exit...")                
        elif option.lower() == 'n':
            question()
        else:
            print("invalid input")


def submit():
    c.execute("INSERT INTO project1_marks VALUES (?,?,?)",(roll_no,quiz,total_marks()))


def export_csv():
    print('export_csv')

#Login Page

print("Welcome !!!")
num=0
while True:
 num = input("1.Login \n2.Register \n3.Quit \nEnter choice to continue : ")
 if num in ['1','2']:
    break
 elif num == '3':
     print("Thank you and be safe :)")
     exit()
 else:
     print("invalid choice enter again :|")

roll_no = 0

if num == '1':

    while True:
        username = input("Username(Roll no) :")
        roll_no = username
        password = input("Password :")
        c.execute(f"SELECT roll,pass FROM project1_registration WHERE roll is '{username}'")
        data = c.fetchall()
        if len(data)>0 and  username == data[0][0] and verify_password(data[0][1],password):
            print("Sucessfully logedin!!!")
            break 
        else:
            print("Wrong credentials!!!")
else:
    while True:
        try:
            name = input("Name:")
            roll = input("Roll no:")
            roll_no = roll
            whatsapp_no = int(input("Whatsapp No.:"))
            password = input("Password:")
            password = hash_password(password)
            c.execute("INSERT INTO project1_registration VALUES (?,?,?,?)",(roll,password,name,whatsapp_no))
            conn.commit()
            print("You are registered and logedin!!!")
            break
        except:
            print("Incorrect inputs!!!")
        

#quiz page 
print("\nChoose your quiz")
quiz_list = os.listdir(os.path.join(os.getcwd(),'quiz_wise_questions'))
quiz_name = [i.split('.')[0] for i in quiz_list]
while True:
    try:
        for i,name in enumerate(quiz_name):
            print(f'{i+1}. {name}')
        print(f"{len(quiz_name)+1}. Quit")
        quiz = int(input("Enter your choice to continue : "))
        break
    except :
        print("Invalid input!!")

if quiz == len(quiz_name) + 1:
    print("Thank You")
    exit()

print('\n',f"{ quiz_name[int(quiz)-1]} loaded!!",'\n')
input("press any key to continue..... ")

file = os.path.join(os.path.join(os.getcwd(),'quiz_wise_questions'),quiz_list[quiz-1])

df = pd.read_csv(file)

c.execute(f"SELECT name_stud FROM project1_registration WHERE roll is '{roll_no}' ")
name = c.fetchone()

t = int(df.columns[-1].split('=')[-1][:-1])*60 #considering time to be in minutes (m)
print(t)
t =t-1
print("name",name,"roll ",roll_no)
p1 = threading.Thread(target=time_dis , args=[t,roll_no,name[0]])
p1.start()
key_map_dict = {'<ctrl>+<alt>+u':unattempted_q,
                '<ctrl>+<alt>+g':goto,
                '<ctrl>+<alt>+f':final_submit,
                '<ctrl>+<alt>+e':export_csv,
               }
listener = keyboard.GlobalHotKeys(key_map_dict)
listener.start()
q_list = list(range(len(df)))
ans = {}
question()




