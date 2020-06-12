import pandas as pd
data = pd.read_csv('tweeter3_data.csv')
data=pd.DataFrame(data)
df = pd.DataFrame()
bol = False
length = len(data)
brk =True
while brk:
    row = data.iloc[:1, :]
    df2 = pd.DataFrame(row)
    user = row.iloc[0]['user_id']
    bool = False
    pos = []
    pos.append(0)
    data2 = data.loc[user]
    print(data2)
    #for index2, row2 in data.iterrows():
    #    if (0 < index2):
    #        user2 = row2['user_id']
    #        if (user == user2):
    #            pos.append(index2)
    #            df3 = pd.DataFrame(data.iloc[index2:index2 + 1, :])
    #            df2 = pd.concat([df2, df3])
    #            # print(df2)
    #            if (row.iloc[0]['location'] != row2['location']):
    #                # print(0,index2)
    #                bool = True
    #                print('yes')
    #    print(index2)

    if (bool == True):
        print('huru')
        df = pd.concat([df, df2])

    print(pos)
    data = data.drop(data.index[pos])
    data = data.reset_index(drop=True)
    if (len(data) == 0):
        print('khela sesh')
        brk = False
        break

print(df)
df.to_csv('final_outcome.csv', index=False)