import pandas as pd
import numpy as np

def group(n=12):
    df = pd.read_csv('Btech_2020_master_data.csv')
    df['branch'] = df['IITP Roll no.'].apply(lambda x : x[4:6])
    branch_list = df.branch.value_counts().to_dict()
    branchSize = list(branch_list.values())
    left = []
    group = []
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
        start = (start + std )%12
    t_group = np.transpose(group)

    #stats file
    g = []
    for i in range(n):
        if i < 9 :
            file = f'Group_G0{i+1}'
        else:
            file = f'Group_G{i+1}'
        g.append(file)
    stats = pd.DataFrame(t_group,columns = list(branch_list.keys()),index = g)
    stats['total'] = [sum(a) for a in t_group]
    stats.to_csv('stats_grouping.csv')

   #for individual group file

    for i in range(n):
        if i < 9 :
            file = f'Group_G0{i+1}.csv'
        else:
            file = f'Group_G{i+1}.csv'
        data = pd.DataFrame()
        for a,s in enumerate(t_group[i]):
            branch = list(branch_list.keys())[a]
            branch_student = df[df.branch == branch][:s]
            #print(branch_student)
            df = df.drop(df[df.branch == branch].index[:s],axis=0)
            data = pd.concat([data,branch_student],axis=0)
        data = data.drop(['branch'],axis=1)
        data = data.reset_index(drop= True)
        data.to_csv(file,index = False)


if __name__ == '__main__':
    while True:
        try:
            n = int(input("Enter the no of groups: "))
            break
        except:
            pass
    group(n)