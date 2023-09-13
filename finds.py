import csv
with open('./enjoysport.csv','r') as f:
    raed = csv.reader(f)
    data = list(raed)
print(data)
at_len = len(data[0])
h =  ['0']*at_len
for row in data:
    if row[-1]=='Yes':
        print('h')
        j=0
        for col in row:
            if col!=h[j] and h[j]=='0':
                h[j]=col
            elif col!=h[j] and h[j]!='0':
                h[j]='?'
            j+=1
print(h)
        