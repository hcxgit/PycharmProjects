#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
def similarity (i,j,k):
   j_neighbors = DG.neighbors(j)   #j 的所有邻居
   j_neighbors.append(j)           #包含j
   k_neighbors = DG.neighbors(k)  #k 的所有邻居
   k_neighbors.append(k)
   j_and_k = set(j_neighbors)&set(k_neighbors)   # 交集
   j_or_k = set(j_neighbors)|set(k_neighbors)    #并集
   S = float(len(j_and_k))/len(j_or_k)
   print '两条边的相似度为',S
G = nx.Graph()
G.add_edges_from([(1,2),(1,3),(1,4),(2,3),(4,5),(2,4),(5,8),(2,8),(8,9),(9,10),(9,11)])  #图
pos = nx.spring_layout(G)
nx.draw(G,pos,with_labels=True)
plt.show()
print '输入节点的值，并显示节点对应的ego网络图'
l = input()
if l in G.nodes():
   node_ego = nx.ego_graph(G, l)   #自我中心节点
   DG = nx.Graph(node_ego)          #节点l的ego网络图
   nx.draw(DG,pos,with_labels=True)
   plt.show()
while True:
   print '请输入两条边的三个节点'
   i = input()
   j = input()
   k = input()
   if (i,j) and (i,k) in DG.edges():
      similarity(i,j,k)
      break
   else:
      print '请重新输入边'