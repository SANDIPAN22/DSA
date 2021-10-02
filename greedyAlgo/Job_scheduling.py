## MAXIMUM JOB 

tasks=[['a',0,6],
        ['b',3,4],
        ['c',1,2],
        ['d',5,8],
        ['e',5,7],
        ['f',8,9]]

tasks.sort(key=lambda k:k[2])
i=tasks[0]
print(i[0])
for j in tasks[1:]:
    if j[1]>i[2]:
        print(j[0])
        i=j
