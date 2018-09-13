# coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from collections import defaultdict
import sys
import seaborn

sys.setrecursionlimit(100000)


# 边相似度计算
def similarity(i, j, k):
    j_neighbors = list(DG.neighbors(j))  # j 的所有邻居
    j_neighbors.append(j)  # 包含j
    k_neighbors = list(DG.neighbors(k))  # k 的所有邻居
    k_neighbors.append(k)
    j_and_k = set(j_neighbors) & set(k_neighbors)  # 交集
    j_or_k = set(j_neighbors) | set(k_neighbors)  # 并集
    S = float(len(j_and_k)) / len(j_or_k)
    return S


fb = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph())
print(nx.info(fb))
pos = nx.spring_layout(fb)
plt.figure()
plt.axis('off')
nx.draw_networkx(fb, pos=pos, with_labels=False, node_size=5)
plt.show()
print ('输入节点的值，并显示节点对应的ego网络图')
l1 = input()
l2 = input()
if l1 and l2 in fb.nodes():
    node_ego1 = nx.ego_graph(fb, l1)  # 自我中心节点
    node_ego2 = nx.ego_graph(fb, l2)
    DG1 = nx.Graph(node_ego1)  # 节点l的ego网络图
    # plt.subplot(121)
    # nx.draw_networkx(DG1)
    DG2 = nx.Graph(node_ego2)
    # plt.subplot(122)
    # nx.draw_networkx(DG2)
    DG = nx.Graph()
    DG.add_edges_from(DG1.edges())
    DG.add_edges_from(DG2.edges())
    pos = nx.spring_layout(DG)
    plt.figure()
    plt.axis('off')
    nx.draw_networkx(DG, pos=pos, with_labels=True)
    plt.show()

    #  相似度矩阵
    s_matix = np.zeros((DG.number_of_edges(), DG.number_of_edges()))
    i = 0
    for x in DG.edges():
        j = 0
        for y in DG.edges():
            if x == y:
                s_matix[i][j] = 1  # 同一条边
            elif x[0] == y[0]:
                s_matix[i][j] = similarity(x[0], x[1], y[1])
            elif x[0] == y[1]:
                s_matix[i][j] = similarity(x[0], x[1], y[0])
            elif x[1] == y[0]:
                s_matix[i][j] = similarity(x[1], x[0], y[1])
            elif x[1] == y[1]:
                s_matix[i][j] = similarity(x[1], x[0], y[0])
            j += 1
        i += 1
    print(s_matix)
    HC = sch.linkage(s_matix, method='single')  # 进行层次聚类
    # HC = sch.complete(s_matix)
    # print(HC)
    plt.figure()
    sch.dendrogram(HC, color_threshold=1, labels=np.array([a for a in DG.edges()]),
                   distance_sort='descending')  # 将层级聚类结果以树状图表示出来
    plt.show()
    cluster = sch.fcluster(HC, t=0.9)  # t取0.75，由HC得到聚类结果:
    membership = list(cluster)
    partition = defaultdict(list)
    for n, p in zip(list(range(DG.number_of_edges())), membership):
        partition[p].append(DG.edges()[n])
    print(partition)
    p = 0
    # color=[(random(),random(),random()) for _i in range(len(partition.keys()))]
    color = []
    for c in seaborn.xkcd_rgb.values():  # 含有颜色的字典
        color.append(c)
    nx.draw_networkx_nodes(DG, pos=pos, node_shape='pie')
    nx.draw_networkx_labels(DG, pos=pos)
    for v in partition.values():
        nx.draw_networkx_edges(DG, pos=pos, edgelist=v, edge_color=color[p])
        p += 1
    plt.show()
    print(list(partition.values()))
