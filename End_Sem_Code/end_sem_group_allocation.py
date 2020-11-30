import pandas as pd
import numpy as np
import os

def group_allocation(filename, number_of_groups):
    try:
        os.mkdir('groups')
    except:
        pass
    n = number_of_groups
    df = pd.read_csv(filename)
    df['branch'] = df['Roll'].apply(lambda x : x[4:6])
    branch_list = df.branch.value_counts().to_dict()
    m = max(branch_list.values())
    eql_br=len([i for i in branch_list.values() if i ==m ])
    branch_name = list(branch_list.keys())[:eql_br]
    branch_name.sort()
    branch_name += list(branch_list.keys())[eql_br:]
    branch_name = [i.upper() for i in branch_name]
    branchSize = list(branch_list.values())
    #strength csv
    strength = pd.DataFrame()
    strength['BRANCH_CODE'] = np.array(branch_name)
    strength['STRENGTH'] = np.array(branchSize)
    strength.to_csv('groups/branch_strength.csv',index = False)
    left = []
    group = []

    for i in branch_name:
        df_temp = df[df.branch == i].copy()
        df_temp = df_temp.drop('branch',axis=1)
        df_temp.to_csv(f'groups/{i}.csv',index = False)

    for i,size in enumerate(branchSize):
        l = [int(size/n) for i in range(n)]
        group.append(l)
        left.append(size - n * int(size/n) )
    start = 0
    group = np.array(group)
    for i,std in enumerate(left):
        group[i][start:start + std] += 1
        if start + std > n:
            l = start + std - n
            group[i][:l] += 1
            start = l
        else:
            start = (start + std )
    t_group = np.transpose(group)

    #stats file
    g = []
    for i in range(n):
        if i < 9 :
            file = f'groups/Group_G0{i+1}'
        else:
            file = f'groups/Group_G{i+1}'
        g.append(file)
    stats = pd.DataFrame(t_group,columns = list(branch_name),index = g)
    stats['total'] = [sum(a) for a in t_group]
    stats.to_csv('groups/stats_grouping.csv')

   #for individual group file

    for i in range(n):
        if i < 9 :
            file = f'groups/Group_G0{i+1}.csv'
        else:
            file = f'groups/Group_G{i+1}.csv'
        data = pd.DataFrame()
        for a,s in enumerate(t_group[i]):
            branch = list(branch_name)[a]
            branch_student = df[df.branch == branch][:s]
            #print(branch_student)
            df = df.drop(df[df.branch == branch].index[:s],axis=0)
            data = pd.concat([data,branch_student],axis=0)
        data = data.drop(['branch'],axis=1)
        data = data.reset_index(drop= True)
        data.to_csv(file,index = False)


filename = "Btech_2020_master_data.csv"
number_of_groups = 10
group_allocation(filename, number_of_groups)