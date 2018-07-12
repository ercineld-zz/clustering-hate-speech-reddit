import pandas as pd
import os

def create_df(path):
    with open(path) as f:
        f = f.read()
    f = f.replace('\\n', '')
    f = f.split('\n')
    L = []
    A = []
    for i in range(0,len(f)-1,3):
        A = [f[i],f[i+1],f[i+2]]
        L.append(A)
    df = pd.DataFrame(L)
    df.columns = ['Subreddit', 'Author', 'Text']
    return df

os.chdir(os.getcwd()+'/main/')
files = os.listdir()
data = []
for i in files:
    frame = create_df(i)
    data.append(frame)
df = pd.concat(data)

df.drop_duplicates(subset = 'Text', keep='first', inplace=True)
df.to_csv('df.csv',sep=',',index=False)
