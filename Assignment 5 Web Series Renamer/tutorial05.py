import os
import re

e_padding = 2 
s_padding = 2

#considering folder in current dir
def rename_FIR(folder_name):
    path = os.path.join(base_dir,folder_name)
    

def rename_Game_of_Thrones(folder_name):
    pass
    
def rename_Sherlock(folder_name = 'Sherlock'):

    path = os.path.join(os.getcwd(),os.path.join('Subtitles',folder_name))
    for file in os.listdir(path):
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
        
    

def rename_Suits(folder_name):
    # rename Logic 
    pass

def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic 
    pass



