# coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from collections import defaultdict
import sys
import seaborn
sys.setrecursionlimit(100000)
# from random import random
# 边相似度计算
def	similarity(i, j, k):
	j_neighbors = DG.neighbors(j)   # j 的所有邻居
	j_neighbors.append(j)           # 包含j
	k_neighbors = DG.neighbors(k)  # k 的所有邻居
	k_neighbors.append(k)
	j_and_k = set(j_neighbors)&set(k_neighbors)   # 交集
	j_or_k = set(j_neighbors)|set(k_neighbors)    # 并集
	S = float(len(j_and_k))/len(j_or_k)
	return S

# fb = nx.read_edgelist("facebook_combined.txt",create_using=nx.Graph())
# 读爬取的数据
with open('circle_edges.txt', 'r') as file:
	f = file.readline()
circle_edgess = [] # 存储 边
ego_me = ''
for k, v in eval(f).items:
	for vs in list(v):
		circle_edgess.append((k,vs))  # 加入发表人和点赞人的边
		circle_edgess.append((ego_me,vs)) # 加入ego节点和点赞人的边
	circle_edgess.append((ego_me,k))  # 加入ego节点和发表人的边
# 将数据整理成ego网络
fb = nx.Graph()
fb.add_edges_from(circle_edgess)
# 画图
# print(nx.info(fb))
# pos = nx.spring_layout(fb)
# plt.figure()
# plt.axis('off')
# nx.draw_networkx(fb,pos=pos,with_labels=False,node_size=5)
# plt.show()
# print ('输入节点的值，并显示节点对应的ego网络图')
# l = input()
if ego_me in fb.nodes():
	node_ego = nx.ego_graph(fb, ego_me)   # 自我中心节点
	DG = nx.Graph(node_ego)          # 节点l的ego网络图
	pos=nx.spring_layout(DG)
	plt.figure()
	plt.axis('off')
	nx.draw_networkx(DG,pos=pos,with_labels=True)
	plt.show()
	print(DG.edges())
	# 相似度矩阵
	s_matix = np.zeros((DG.number_of_edges(), DG.number_of_edges()))
	i = 0
	for x in DG.edges():
		j = 0
		for y in DG.edges():
			if x == y:
				s_matix[i][j] = 1  # 同一条边
			elif x[0] == node_ego and y[0] == node_ego:  # 共同节点为ego节点
				s_matix[i][j] = similarity(x[0], x[1], y[1])
			elif x[0] == node_ego and y[0] != node_ego:  # 共同节点不是ego节点，y的边为侧边
				if x[1] == y[1]:
					s_matix[i][j] = similarity(x[1], x[0], y[0])
				elif x[1] == y[0]:
					s_matix[i][j] = similarity(x[1], x[0], y[1])
			elif x[0] != node_ego and y[0] == node_ego:  # 共同节点不是ego节点,x为侧边
				if x[0] == y[1]:
					s_matix[i][j] = similarity(x[0], x[1], y[0])
				elif x[1] == y[1]:
					s_matix[i][j] = similarity(x[1], x[0], y[0])
			elif x[0] != node_ego and y[0] != node_ego:  # 共同节点不是ego节点,x,y都为侧边
				if x[0] == y[0]:
					s_matix[i][j] = similarity(x[0], x[1], y[1])
				elif x[0] == y[1]:
					s_matix[i][j] = similarity(x[0], x[1], y[0])
				elif x[1] == y[0]:
					s_matix[i][j] = similarity(x[1], x[0], y[1])
				elif x[1] == y[1]:
					s_matix[i][j] = similarity(x[1], x[0], y[0])
			j += 1
		i += 1
	print(len(s_matix))
	HC = sch.linkage(s_matix, method='complete')  # 进行层次聚类
	print(type(HC))
	print(HC)
	plt.figure()
	sch.dendrogram(HC, color_threshold=1, truncate_mode='lastp', labels=np.array([a for a in DG.edges()]),
				distance_sort='descending')  # 将层级聚类结果以树状图表示出来

	plt.gca().invert_yaxis()
	plt.show()

	# cluster = sch.fcluster(HC, t=0.9)  # t取0.75，由HC得到聚类结果:
	# membership = list(cluster)
	# partition = defaultdict(list)
	# for n, p in zip(list(range(DG.number_of_edges())), membership):
	# 	partition[p].append(DG.edges()[n])
	# print(partition)
	# p = 0
	# color = []
	# for c in seaborn.xkcd_rgb.values():  # 含有颜色的字典
	# 	color.append(c)
	#
	# for v in partition.values():
	# 	for n in v:
	# 		nx.draw_networkx_nodes(DG, pos=pos, nodelist=list(n), node_color=color[p])
	# 		nx.draw_networkx_labels(DG, pos=pos)
	# 	nx.draw_networkx_edges(DG, pos=pos, edgelist=v)
	# 	p += 1
	# plt.show()
	# print(list(partition.values()))
