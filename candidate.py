import csv
with open('./enjoysport.csv','r') as f:
    raed = csv.reader(f)
    data = list(raed)
print(data)

at_len = len(data[0])
G = ['?']*at_len
S = ['0']*at_len
temp = []

for row in data :
    if row[-1] == 'Yes':
        j=0
        for col in row:
            if col!='Yes':
                if col!=S[j] and S[j]=='0':
                    S[j]=col
                if col!=S[j] and S[j]!='0':
                    S[j]='?'
                j+=1
        for j in range(0,at_len):
            for k in temp:
                if k[j]!=S[j] and k[j]!='?':
                    temp.remove(k)

        
    if row[-1] == 'No':
        j=0
        for col in row:
            
            if col!='No':
                if col!=S[j] and S[j]!='?':
                    G[j]=S[j]
                    temp.append(G)
                    G = ['?']*at_len
                j+=1
print(S)
print(temp)




