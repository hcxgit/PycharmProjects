#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
'''
G = nx.random_partition_graph([10,10],0.5,0.5)
nx.draw(G)
plt.show()
'''
G = nx.Graph()
G.add_node(10)
#H = nx.path_graph(10)
#G.add_nodes_from(H)
G.add_edge(1,2)
G.add_edges_from([(2,3),(4,5)])
#G.add_edges_from(H.edges())
print '节点个数为：' ,G.number_of_nodes()
print '边个数为：', G.number_of_edges()
print '图中有这些点：',G.nodes()
print '图中有这些边：',G.edges()
print '节点1的邻居结点为：',G.neighbors(1)
G.remove_node(10)
print '移除10这个节点后，节点的个数为：',G.nodes()
G.add_edge(1,5,{'weight':10})
G.add_edge(1,4,{'len':10})
print G[1]
print G[1][4]
print '*********'
for index in G.edges_iter(data=True):
	print index
G[1][4]['len']=20
print G[1][4]
#用邻接迭代器快速遍历每一条边
print '###############'
FG = nx.Graph()
FG.add_weighted_edges_from([(1,2,0.125),(1,3,0.75),(2,4,0.12),(3,4,0.375)])
for n,nbr in FG.adjacency_iter():  #返回一个dic  例如 n=1,时，FG.adjacency_iter()返回值为（1，2：{weight：0.125}，3:{weight:0.75}）
	print 'n为',n                  #把1 给n,   把{2：{weight：0.125}，3:{weight:0.75}}给 nbr
	print '***nbr为',nbr
	for nbrs,eattr in nbr.items():  # items() 函数以列表返回可遍历的(键, 值) 元组数组
		data = eattr['weight']     #eattr   属性
		print 'eattr为',eattr
		if data < 0.5:
			print '%d,%d,%.3f'%(n,nbrs,data)
		print '$$$$'

# 一种方便的访问所有边的方法
print '!!!!!!!!!!!!!!'
for(u,v,d) in FG.edges(data = 'weight'):
	print (u,v,d)
#####有向图
print '有向图'
DG = nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5),(1,3,1.1),(4,1,2.3),(4,5,10)])
print DG.out_degree(1)   #  1的出度
print DG.out_degree(1,weight='weight')  #1的所有出度权值之和
print DG.degree(1)       #结点1的度
print DG.successors(1)   #结点1的继承者
print DG.neighbors(1)    #结点1的邻居（不包括指向1的点）
#####显示图
nx.draw(DG)
nx.draw_random(DG)   	# 随机图布局         布局也可以用pos = nx.random_layout
nx.draw_circular(DG)	#圆形布局图
nx.draw_spectral(DG)	#光谱（拉普拉斯特征向量）图布局
plt.show()

'''
#######有向图转换为无向图
H = nx.Graph(DG)     	#或者   H=DG.to_undirected()
#######随机图发生器
er=nx.erdos_renyi_graph(100,0.15)  			# ER随机图
ws=nx.watts_strogatz_graph(30,3,0.1) 		# WS小世界图
ba=nx.barabasi_albert_graph(100,5)			# BA无标度图
red=nx.random_lobster(100,0.9,0.9)
nx.draw(er)
nx.draw(ws)
nx.draw(ba)
nx.draw(red)
plt.show()
'''

ws=nx.watts_strogatz_graph(15,2,0.1) 		# WS小世界图
nx.draw(ws)
plt.show()
