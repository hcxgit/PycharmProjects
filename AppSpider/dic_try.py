#coding:utf-8
# a = {'张三': ['张三']}
# b = '李四'
# c = '网吧'
# # for k in list(a.keys()):
# # 	if b in k:
# # 		a[b].append(c)
# # 	else:
# # 		a.setdefault(b, [])
# # 		a[b].append(c)
# # 		print(a[b])
# # 		print("222")
# a.setdefault(b, []).append(c)
# print(a)
# a = '张三，李四，王五'
# b = '王八'
# a = a.split('，')
# print(a)
# print(b.split('，'))
# a={'张三':'李四'}
# with open('circle_edges.txt','w') as file:
# 	file.write(repr(a))
# with open(r'H:\新建文件夹 (2)\PycharmProjects\AppSpider\circle_edges.txt', 'r') as file:
# 	f = eval(file.readline())
# circle_edgess = []  # 存储 边
# ego_me = '带拉格朗日余项的平衡二叉树'
# for k, v in f.items():
# 	for vs in list(v):
# 		circle_edgess.append((k, vs.lstrip()))  # 加入发表人和点赞人的边
# 		circle_edgess.append((ego_me, vs.lstrip()))  # 加入ego节点和点赞人的边
# 	circle_edgess.append((ego_me, k))  # 加入ego节点和发表人的边
# print(circle_edgess)
# # print(type(f))

a = ['暖阳']
b = ['陈灿', '余生', '蒙', 'i want', 'A张新新']
c = ['小ｖ', '双手合十亦步亦趋']
d = ['贺自信', '嘿嘿', '泰宁先生', '王豪18661847581']
e = ['Shaun', '郭文娜']
f = ['吴小胖']
g = ['姐姐', 'YUAN', '张倩']

print("初中:", a)
print("高中:", b)
print("本科:", c)
print("现在班级:", d)
print("研究生:", e)
print("老乡:", f)
print("家人:", g)

# import matplotlib.pyplot as plt
# import numpy as np
# import scipy.cluster.hierarchy as sch
# from collections import defaultdict
# import sys
# import seaborn
# import gc
# from sklearn import metrics
# sys.setrecursionlimit(100000)
# from pylab import *
# import networkx as nx
# # 边相似度计算
# def	similarity(i, j, k, DG):
# 	j_neighbors = list(DG.neighbors(j))   # j 的所有邻居
# 	j_neighbors.append(j)           # 包含j
# 	k_neighbors = list(DG.neighbors(k))  # k 的所有邻居
# 	k_neighbors.append(k)
# 	j_and_k = set(j_neighbors)&set(k_neighbors)   # 交集
# 	j_or_k = set(j_neighbors)|set(k_neighbors)    # 并集
# 	S = float(len(j_and_k))/len(j_or_k)
# 	return S
#
# #  相似度矩阵
# def	similarity_matix(edges, longth_edges, DG):
# 	# 相似度矩阵   第0行和第0列表示类的代号
# 	#s_matix = np.zeros((longth_edges+1, longth_edges+1))
# 	s_matix = [[0 for i in range(longth_edges+1)] for i in range(longth_edges+1)]
# 	for i in range(1,len(s_matix)):
# 		s_matix[0][i] = i-1
# 		s_matix[i][0] = i-1
# 	i = 1
# 	for x in edges:
# 		j = 1
# 		for y in edges:
# 			# 同边
# 			if x == y:
# 				s_matix[i][j] = 1
# 			# 有共同点
# 			elif x[0] == y[0]:
# 				s_matix[i][j] = similarity(x[0], x[1], y[1], DG)
# 			elif x[0] == y[1]:
# 				s_matix[i][j] = similarity(x[0], x[1], y[0], DG)
# 			elif x[1] == y[0]:
# 				s_matix[i][j] = similarity(x[1], x[0], y[1], DG)
# 			elif x[1] == y[1]:
# 				s_matix[i][j] = similarity(x[1], x[0], y[0], DG)
# 			# 没有共同点
# 			else:
# 				s_matix[i][j] = 0
# 			j += 1
# 		i += 1
# 	return s_matix
#
# # 用最近邻方法合并类，更新矩阵
# def	distances(a, b, c, s_matix):
# 	for i in range(1, len(s_matix)):
# 		s_matix[a][i] = s_matix[i][a] = max(s_matix[a][i], s_matix[b][i])  # a、b的内容取值放入a
# 	s_matix[a][0] = s_matix[0][a] = c  	 			# 类代号改变
# 	s_matix = np.delete(s_matix, b, axis=0)			# 删除b
# 	s_matix = np.delete(s_matix, b, axis=1)
# 	return s_matix
#
# # 分区密度  m：边数，n：点数
# def	density(m, n):
# 	try:
# 		return 2*(m-n+1.0)/(n-2.0)/(n-1.0)
# 	except ZeroDivisionError: 			 # 分母为0
# 		return 0.0
#
# # 平均分区密度
# def	ave_Density(density_list, edges, clusters):
# 	sum = 0
# 	for i, element in enumerate(density_list):
# 		sum += element*len(clusters[i])
# 	return sum/len(edges)
# # 聚类函数
# def	clustering(s_matix, edges, max_density):
# 	clusters = [[0 for col in range(0, len(s_matix)-1)]for row in range(0, len(s_matix)-1)]      # 初始化n个类
# 	# HC = []          			 		 			# 用来和树状图对接
# 	density_list = []  								# 分区密度列表
# 	for i in range(0, len(s_matix)-1):  			# 初始化聚类列表和分区密度列表
# 		clusters[i] = [edges[i]]
# 		density_list.append(density(1, 2))
# 	ave_density_list = []     					 	# 平均分区密度列表
# 	ave_density_list.append(ave_Density(density_list, edges, clusters))
#
# 	num_clusters = len(s_matix)-1  					# 合并类的代号
# 	if max_density == 0:							# 标志位   传进来的max_density 为0，则聚类为一个  否则按照max_density聚类
# 		while len(clusters) > 1:   			 		# 判断聚类是否完成
# 			max_similar = 0
# 			point1 = 1
# 			point2 = 1
# 			for i in range(1, len(s_matix)-1):
# 				for j in range(i+1, len(s_matix)):
# 					if s_matix[i][j] >= max_similar:
# 						max_similar = s_matix[i][j]
# 						point1 = i
# 						point2 = j
# 					else:
# 						continue
#
# 			for c in clusters[point2-1]:               # 将合并的类归入
# 				clusters[point1-1].append(c)
#
# 			del density_list[point2-1]				   # 更新density_list
# 			density_list[point1-1] = density(len(clusters[point1-1]), len(list(np.unique(clusters[point1-1]))))
# 			ave_density_list.append(ave_Density(density_list, edges, clusters))  # 更新ave_density_list
#
# 			# hc = [s_matix[0][point1], s_matix[0][point2], max_similar, len(clusters[point1-1])]
# 			# HC.append(hc)
# 			s_matix = distances(point1, point2, num_clusters, s_matix)  # 合成相似度最大的两个类,改变矩阵
# 			clusters = np.delete(clusters, point2-1, axis=0)   # 类的总数减少了一个
# 			num_clusters += 1
# 			#c.collect()
# 	else:
# 		max_similar = 1
# 		while max_similar >= max_density:  # 判断聚类是否完成
# 			max_similar = 0
# 			point1 = 1
# 			point2 = 1
# 			for i in range(1, len(s_matix) - 1):
# 				for j in range(i + 1, len(s_matix)):
# 					if s_matix[i][j] >= max_similar:
# 						max_similar = s_matix[i][j]
# 						point1 = i
# 						point2 = j
# 					else:
# 						continue
#
# 			for c in clusters[point2 - 1]:  # 将合并的类归入
# 				clusters[point1 - 1].append(c)
#
# 			del density_list[point2 - 1]  # 更新density_list
# 			density_list[point1 - 1] = density(len(clusters[point1 - 1]), len(list(np.unique(clusters[point1 - 1]))))
# 			ave_density_list.append(ave_Density(density_list, edges, clusters))  # 更新ave_density_list
#
# 			# hc = [s_matix[0][point1], s_matix[0][point2], max_similar, len(clusters[point1 - 1])]
# 			# HC.append(hc)
# 			s_matix = distances(point1, point2, num_clusters, s_matix)  # 合成相似度最大的两个类,改变矩阵
# 			clusters = np.delete(clusters, point2 - 1, axis=0)  # 类的总数减少了一个
# 			num_clusters += 1
#
# #  将划分的社区以每个节点所属社区的形式表示
# def	node_circle(clusters2,frinds):
# 	frinds2 = frinds[:]
# 	for f in frinds:
# 		id = 0  		# 社区id
# 		max_len = 0  		# 每个节点所属最大社区的长度
# 		for i in list(clusters2):
# 			lens = len(clusters2[id])
# 			for j in i:
# 				if str(f) in j:
# 					if lens >= max_len:
# 						frinds2[frinds.index(int(f))] = id
# 						max_len = lens
# 					break
# 			id += 1
# 	return frinds2
# if __name__ == "__main__":
# 	plt.figure()
# 	plt.axis('off')
# 	g=nx.Graph()
#
# 	circle_edgess=[('Shaun', '郭文娜'), ('带拉格朗日余项的平衡二叉树', '郭文娜'), ('带拉格朗日余项的平衡二叉树', 'Shaun'), ('面面', '戴婷'), ('带拉格朗日余项的平衡二叉树', '戴婷'), ('带拉格朗日余项的平衡二叉树', '面面'), ('陈灿', '余生'), ('带拉格朗日余项的平衡二叉树', '余生'), ('带拉格朗日余项的平衡二叉树', '陈灿'), ('余生', 'A张新新'), ('带拉格朗日余项的平衡二叉树', 'A张新新'), ('带拉格朗日余项的平衡二叉树', '余生'), ('小ｖ', '双手合十の亦步亦趋'), ('带拉格朗日余项的平衡二叉树', '双手合十の亦步亦趋'), ('带拉格朗日余项的平衡二叉树', '小ｖ'), ('张倩', '姐姐'), ('带拉格朗日余项的平衡二叉树', '姐姐'), ('带拉格朗日余项的平衡二叉树', '张倩'), ('姐姐', 'YUAN'), ('带拉格朗日余项的平衡二叉树', 'YUAN'), ('带拉格朗日余项的平衡二叉树', '姐姐'), ('暖阳', '暖阳'), ('带拉格朗日余项的平衡二叉树', '暖阳'), ('带拉格朗日余项的平衡二叉树', '暖阳'), ('贺自信', '嘿嘿～'), ('带拉格朗日余项的平衡二叉树', '嘿嘿～'), ('贺自信', '王豪-18661847581'), ('带拉格朗日余项的平衡二叉树', '王豪-18661847581'), ('贺自信', '泰宁先生'), ('带拉格朗日余项的平衡二叉树', '泰宁先生'), ('带拉格朗日余项的平衡二叉树', '贺自信'), ('蒙', 'A张新新'), ('带拉格朗日余项的平衡二叉树', 'A张新新'), ('蒙', '带拉格朗日余项的平衡二叉树'), ('带拉格朗日余项的平衡二叉树', '带拉格朗日余项的平衡二叉树'), ('蒙', '陈灿'), ('带拉格朗日余项的平衡二叉树', '陈灿'), ('蒙', 'i want'), ('带拉格朗日余项的平衡二叉树', 'i want'), ('带拉格朗日余项的平衡二叉树', '蒙')]
# 	g.add_edges_from(circle_edgess)
# 	nx.draw_networkx(g, with_labels=True)
# 	plt.show()
# 	ego_me = '带拉格朗日余项的平衡二叉树'
# 	if ego_me in g.nodes():
# 		node_ego = nx.ego_graph(g, ego_me)
# 		DG = nx.Graph(node_ego)
# 	s_matix = np.array(similarity_matix(DG.edges(), DG.number_of_edges(), DG))
# 	# ++++++++++++++++++++++++++++++++++
# 	clusters, ave_density_list = clustering(s_matix, DG.edges(), 0)  # 聚为一个类，得到最大分区密度
#
# # 画图
#
# 	clusters2 = list(clusters2)
# 	p = 0
# 	color = []
# 	for c in seaborn.xkcd_rgb.values():  # 含有颜色的字典
# 		color.append(c)
# 	pos = nx.spring_layout(DG)
# 	for v in clusters2:
# 		for n in v:
# 			nx.draw_networkx_nodes(DG, pos=pos, nodelist=list(n), node_size=50)
# 			nx.draw_networkx_labels(DG, pos=pos, font_size=6)
# 		nx.draw_networkx_edges(DG, pos=pos, edgelist=v, edge_color=color[p])
# 		p += 4
# 	plt.show()



