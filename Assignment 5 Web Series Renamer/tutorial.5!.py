import os
import re

e_padding = 2
s_padding = 2


def rename_Sherlock(folder_name = 'Sherlock'):
    path = os.path.join(os.getcwd(),os.path.join('Subtitles',folder_name))
    for file in os.listdir(path):
        try:
            name = file.split('.')
            if 'E' not in name[1]:
                season = (s_padding - len(name[1][1:].replace('0','')))*'0' + name[1][1:].replace('0','')
                episode = (e_padding - len(name[2][1:].replace('0','')))*'0' + name[2][1:].replace('0','')
            else:
                block = name[1].split("E")
                season = (s_padding - len(block[0][1:].replace('0','')))*'0' + block[0][1:].replace('0','')
                episode = (e_padding - len(block[1].replace('0','')))*'0' + block[1].replace('0','')
            file_name = name[0] + " - Season " + season + " Episode " + episode + "." + name[-1]
            file_name = os.path.join(path,file_name)
            file_name_old = os.path.join(path,file)
            print(file_name)
            os.rename(file_name_old,file_name)



def rename_Suits(folder_name = 'Suits'):
    path = os.path.join(os.getcwd(),os.path.join('Subtitles',folder_name))
    for file in os.listdir(path):
    try:
    name = file.split('-')
    name = [i.strip() for i in name]
    season = (s_padding - len(name[1].split('x')[0].replace('0','')))*'0' + name[1].split('x')[0]
    episode = (e_padding - len(name[1].split('x')[1].replace('0','')))*'0' + name[1].split('x')[1]
    episode_name = name[-1]split('.')[0].strip()
    ext = name[-1]split('.')[-1]
    file_name = name[0] + " - Season " + season + " Episode " + episode + " - " + episode_name + "." + ext
    print(file_name)
    # file_name_old = os.path.join(path,file)
    # file_name = os.path.join(path,file_name)
    # os.rename(file_name_old,file_name)
