import sys
INF=sys.maxsize
def printGraph(nv,G):
    for i in range(nv):
        for j in range(nv):
            if G[i][j]==INF:
                print("INF", end=' ')
            else:
                print(G[i][j],end=' ')
        print()

def apsp(nv,G):
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                G[i][j]=min(G[i][j],G[i][k]+G[k][j])

G=[[0,8,INF,1],
    [INF,0,1,INF],
    [4,INF,0,INF],
    [INF,2,9,1]
    ]

printGraph(4,G)
apsp(4,G)
print()
printGraph(4,G)