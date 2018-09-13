# coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from collections import defaultdict


def similarity(i, j, k):
    j_neighbors = DG.neighbors(j)  # j 的所有邻居
    j_neighbors.append(j)  # 包含j
    k_neighbors = DG.neighbors(k)  # k 的所有邻居
    k_neighbors.append(k)
    j_and_k = set(j_neighbors) & set(k_neighbors)  # 交集
    j_or_k = set(j_neighbors) | set(k_neighbors)  # 并集
    S = float(len(j_and_k)) / len(j_or_k)
    # print ('两条边的相似度为',S)
    return S


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (1, 4), (2, 3), (4, 5), (2, 4), (5, 8), (2, 8), (8, 9), (9, 10), (9, 11)])  # 图
pos = nx.spring_layout(G)
plt.figure()  # 创建一个显示窗口
plt.axis('off')  # 不显示坐标
nx.draw_networkx(G, pos, with_labels=True)
plt.show()
print(G.nodes())
print ('输入节点的值，并显示节点对应的ego网络图')
l = int(input())
if l in G.nodes():
    node_ego = nx.ego_graph(G, l)  # 自我中心节点
    DG = nx.Graph(node_ego)  # 节点l的ego网络图
    plt.figure()
    plt.axis('off')
    nx.draw_networkx(DG, pos, with_labels=True)
    plt.show()
    print(DG.edges())
    s_matix = np.zeros((DG.number_of_edges(), DG.number_of_edges()))
    i = 0
    for x in DG.edges():
        j = 0
        for y in DG.edges():
            if x == y:
                s_matix[i][j] = 1  # 同一条边
            if x[0] == node_ego and y[0] == node_ego:  # 共同节点为ego节点
                s_matix[i][j] = similarity(x[0], x[1], y[1])
            if x[0] == node_ego and y[0] != node_ego:  # 共同节点不是ego节点，y的边为侧边
                if x[1] == y[1]:
                    s_matix[i][j] = similarity(x[1], x[0], y[0])
                if x[1] == y[0]:
                    s_matix[i][j] = similarity(x[1], x[0], y[1])
            if x[0] != node_ego and y[0] == node_ego:  # 共同节点不是ego节点,x为侧边
                if x[0] == y[1]:
                    s_matix[i][j] = similarity(x[0], x[1], y[0])
                if x[1] == y[1]:
                    s_matix[i][j] = similarity(x[1], x[0], y[0])
            if x[0] != node_ego and y[0] != node_ego:  # 共同节点不是ego节点,x,y都为侧边
                if x[0] == y[0]:
                    s_matix[i][j] = similarity(x[0], x[1], y[1])
                if x[0] == y[1]:
                    s_matix[i][j] = similarity(x[0], x[1], y[0])
                if x[1] == y[0]:
                    s_matix[i][j] = similarity(x[1], x[0], y[1])
                if x[1] == y[1]:
                    s_matix[i][j] = similarity(x[1], x[0], y[0])
            j += 1
        i += 1
    print(s_matix)
    Z = sch.linkage(s_matix, method='single')  # 进行层次聚类
    print(Z)
    plt.figure()
    plt.subplot(1, 2, 1)
    sch.dendrogram(Z, color_threshold=1, labels=np.array([a for a in DG.edges()]),
                   distance_sort='descending')  # 将层级聚类结果以树状图表示出来
    plt.show()
    cluster = sch.fcluster(Z, t=0.8)  # 根据linkage matrix Z得到聚类结果:
    membership = list(cluster)
    partition = defaultdict(list)
    for n, p in zip(list(range(DG.number_of_edges())), membership):
        partition[p].append(DG.edges()[n])
    p = 0
    for v in partition.values():
        p += 1
        print(v)
        nx.draw_networkx_edges(DG, pos=pos, edgelist=v, edge_color=3)
    plt.show()
    print(list(partition.values()))
