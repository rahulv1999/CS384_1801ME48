import sqlite3
import hashlib, binascii, os
import  time
import pandas as pd
from pynput import keyboard
import threading
import re
from pynput.keyboard import Key, Controller,Listener
key_board = Controller()
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
    for q in q_list2:
        if q in q_list:
            a = dis_q(q)
            if(a):
                ans[q]=a
            else:
                goto(0)
    if len(q_list)==0:
        print("you have attempted all the questions")
        final_submit()
    if len(q_list):
        question()


def next(q_no):
    no = q_list.index(q_no)
    if no <len(q_list)-1:
        return no+1
    else:
        return 0

def p(key):
    pass

def p2(key):
    print(key)
    print("try this")

def dis_q(q_no,g=0):

    if q_no <= len(df):
        # input("press any key for the question..")
        print('\n',f'Q{q_no + 1})', df.question[q_no],'\n',\
            'option1)',df.option1[q_no],'\n','option2)',df.option2[q_no],'\n',\
                'option3)',df.option3[q_no],'\n',\
            'option4)',df.option4[q_no],'\n')
        # time.sleep(10)


        while True:
            listener = keyboard.GlobalHotKeys({'<ctrl>+<alt>+g':goto})
            listener.start()
            x = input("Enter your choice 1,2,3,4,S(skip): ")
            try:
                listener.stop()
            except:
                pass
            pat = re.compile(r'ṅ')
            if re.match(pat,x):
                if not g:
                    return 0
                else:
                    goto(0)
            try:
                x = int(x)
                if x in range(1,5):
                    if q_no in q_list:
                        q_list.remove(q_no)
                    ans[q_no] =x
                    break
                else:

                    print("invalid choice enter again")
            except:
                if type(x)!=int and  x.lower() == 's':
                    if len(q_list)>1:
                        dis_q(next(q_no))

                    else:
                        input("no more question to skip...use '<ctrl>+<alt>+g' \
                             to goto question no or press any other key to continue...")
                        question()
                else:
                    print("invalid choice enter again")
        try:
            listener.stop()
        except:
            pass
        return x
    else:
        print(f"there are only {len(df)} questions, choose accordingly..")


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
    conn = sqlite3.connect('project1 quiz cs384.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE  project1_registration (
                            roll text,
                            pass text,
                            name_stud text,
                            whatsapp_no number

                                        )""")
    conn.commit()

except :
    print
try:
    conn = sqlite3.connect('project1 quiz cs384.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE  project1_marks (
                            roll text,
                            quiz_num number,
                            total_marks number
                                        )""")
    conn.commit()
except :
    print


def unattempted_q():
    print('\n',f'there are {len(q_list)} unattempted question(s) ')

def goto(f=1):
    if f:
        key_board.press(Key.enter)
        print("\n enter the question number",end='\r')
        # while True:
        #     k = input(("\nenter the question numer : "))
        #     try:
        #         q_no = int(k)
        #         break
        #     except:
        #         print("invalid input..")
        # dis_q(q_no-1)
        # pass
    else:
        l = 0
        while True:

            if l:
                k = input(("\nenter the question number : "))
            else:
                k = input("here..")

            try:
                q_no = int(k)
                break
            except:
                l=1
                print("invalid input..")
        dis_q(int(q_no)-1,1)

def total_marks():
    marks = 0
    correct =0
    wrong =0
    for i in range(len(df)):
        if i in list(ans.keys()):
            if int(ans[i]) == int(df.correct_option[i]):
                marks += int(df.marks_correct_ans[i])
                correct +=1
            else:
                marks += int(df.marks_wrong_ans[i])
                wrong +=1
        else:
            if df.compulsory[i] == 'y':
                 marks += int(df.marks_wrong_ans[i])
    return marks,correct,wrong


def stats():
    marks,correct,wrong = total_marks()
    print("\nTotal Quiz Questions:",len(df))
    print("Total Quiz Questions Attempted:",len(quiz_list))
    print("Total Correct Question:",correct)
    print("Total Wrong Questions:",wrong)
    print("Total Marks: obtained marks/total marks",marks)

def final_submit():
    while True:
        option =  input(' Do you want to final submit? (y/n) ')
        if option.lower() == 'y':
            print("Submitted Thankyou ...")
            submit()
            stats()
            print("press Ctrl+Alt+E to export data to csv")
            input("press any key to exit...")
            break
        elif option.lower() == 'n' :
            if len(q_list)==0:
                print("""you have attempted all the questions
press Ctrl+Alt+G to goto a question or
press any other button to exit""",end="")
                input("....")
                break
            if len(q_list):
                question()
        else:
            print("invalid input")


def submit():
    marks,_,_ = total_marks()
    conn = sqlite3.connect('project1 quiz cs384.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM project1_marks WHERE roll={roll_no} and quiz_num = {quiz}")
    if len(list(c.fetchall()))==0:
        c.execute("INSERT INTO project1_marks VALUES (?,?,?)",(roll_no,quiz,marks))
    else:
        c.execute(f"UPDATE project1_marks SET total_marks={marks} \
            WHERE roll={roll_no} and quiz_num = {quiz}")
    conn.commit()



def export_csv():
    conn = sqlite3.connect('project1 quiz cs384.db')
    c = conn.cursor()
    c.execute(f"SELECT * FROM project1_marks WHERE quiz_num=={quiz}")
    df = pd.DataFrame(c.fetchall(),columns = ['roll_no','quiz','total_marks'])
    file = os.path.join(os.path.join(os.getcwd(),'quiz_wise_responses'),f"scores_q{quiz}.csv")
    df.to_csv(file)

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
        conn = sqlite3.connect('project1 quiz cs384.db')
        c = conn.cursor()
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
        if quiz<= len(quiz_name)+1:
            break
        else:
            print("Invalid input!!")
    except :
        print("Invalid input!!")

if quiz == len(quiz_name) + 1:
    print("Thank You")
    exit()

print('\n',f"{ quiz_name[int(quiz)-1]} loaded!!",'\n')


file = os.path.join(os.path.join(os.getcwd(),'quiz_wise_questions'),quiz_list[quiz-1])

df = pd.read_csv(file)

c.execute(f"SELECT name_stud FROM project1_registration WHERE roll is '{roll_no}' ")
name = c.fetchone()

t = int(df.columns[-1].split('=')[-1][:-1])*60 #considering time to be in minutes (m)

t =t-1

key_map_dict = {'<ctrl>+<alt>+u':unattempted_q,
                '<ctrl>+<alt>+g':goto,
                '<ctrl>+<alt>+f':final_submit,
                '<ctrl>+<alt>+e':export_csv,
               }
# listener = keyboard.GlobalHotKeys(key_map_dict)
# # listener.start()
# # listener =  keyboard.Listener(on_press=p2,on_release=p)
# # listener.start()
# lis(1,listener)
q_list = list(range(len(df)))
q_list2 = list(range(len(df)))
ans = {}
question()
# p1.join()



