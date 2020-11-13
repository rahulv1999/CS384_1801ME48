import os
import re

e_padding = 2
s_padding = 2

def rm_zero(s):
    s = s.strip()
    if s[0]=='0':
        for i in range(1,len(s)):
            if s[i] !='0':
                return s[i:]
    else:
        return s


#considering folder in current dir
def rename_FIR(folder_name):
    # path = os.path.join(os.getcwd(),os.path.join('Subtitles',folder_name))
    # for file in os.listdir(path):
    #     name = file.split('-')
    #     ext = name[-1].split('.')[-1]
    #     episode =
    #     head = "FIR - "  + name
    pass


def rename_Game_of_Thrones(folder_name):
    pass

def rename_Sherlock(folder_name = 'Sherlock'):
    path = os.path.join(os.getcwd(),os.path.join('Subtitles',folder_name))
    for file in os.listdir(path):
        try:
            name = file.split('.')
            if 'E' not in name[1]:
                season = (s_padding - len(rm_zero(name[1][1:])))*'0' + rm_zero(name[1][1:])
                episode = (e_padding - len(rm_zero(name[2][1:])))*'0' + rm_zero(name[2][1:])
            else:
                block = name[1].split("E")
                season = (s_padding - len(rm_zero(block[0][1:])))*'0' + rm_zero(block[0][1:])
                episode = (e_padding - len(rm_zero(block[1])))*'0' + rm_zero(block[1])
            file_name = name[0] + " - Season " + season + " Episode " + episode + "." + name[-1]
            file_name = os.path.join(path,file_name)
            file_name_old = os.path.join(path,file)
            print(file_name)
            os.rename(file_name_old,file_name)
        except :
            pass





# def rename_How_I_Met_Your_Mother(folder_name):
#     # rename Logic
#     pass




def rename_Suits(folder_name = 'Suits'):
    path = os.path.join(os.getcwd(),os.path.join('Subtitles',folder_name))
    for file in os.listdir(path):
        try:
            name = file.split('-')
            name = [i.strip() for i in name]
            season = (s_padding - len(rm_zero(name[1].split('x')[0])))*'0' + rm_zero(name[1].split('x')[0])
            episode = (e_padding - len(rm_zero(name[1].split('x')[1])))*'0' +rm_zero(name[1].split('x')[1])
            if len(name)==3:
                episode_name = name[-1].split('.')[0].strip()
            else:
                episode_name = name[-2].split('.')[0].strip()
            ext = name[-1].split('.')[-1]
            file_name = name[0] + " - Season " + season + " Episode " + episode + " - " + episode_name + "." + ext
            file_name_old = os.path.join(path,file)
            file_name = os.path.join(path,file_name)
            try:
                os.rename(file_name_old,file_name)
            except:
                os.remove(file_name_old)
        except:
            pass




rename_Suits()