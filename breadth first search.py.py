from queue import Queue
adj_list={'A':['B','D'],
          'B':['A','C'],
          'C':['D'],
          'D':['A','E','f'],
          'E':['D','F','G'],
          'F':['D','E','H'],
          'G':['E','H'],
          'H':['F','G']}
visited={}
parent={}
level={}
dfs_out=[]
queue=Queue()
for node in adj_list.keys():
   visited[node]=False
   parent[node]=None
   level[node]=-1
S='A'
visited[S]=True   
level[S]=0
queue.put(S)
while not queue.empty():
    u=queue.get()
    dfs_out.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.put(v)
print(dfs_out)
print(level)
v='G'
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path.reverse()
print(path) 