m = [[2,3,4,5,],[1,9,8,7],[11,15,65,18]]
#print(m)
tr_m = [[0 for j in range(len(m))] for i in range(len(m[0]))]
#print(tr_m)
for i in range(len(m)):
    for j in range(len(m[0])):
        tr_m[j][i]=m[i][j]
print('изначальная матрица:\n',*m,'\n')

print('__________________________________________________\n')
print("Транспортрованная матрица:\n",*tr_m)