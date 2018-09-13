# coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from collections import defaultdict
import sys
import seaborn

sys.setrecursionlimit(100000)
import collections
import re


# import Test_9.facebook4 as face
def edges():
    fb = nx.read_edgelist(r"D:\新建文件夹 (2)\PycharmProjects\Test_9\facebook_combined.txt", create_using=nx.Graph())
    l = '3980'
    if l in fb.nodes():
        node_ego = nx.ego_graph(fb, l)  # 自我中心节点
        DG = nx.Graph(node_ego)  # 节点l的ego网络图
        return DG, l


# pos = nx.spring_layout(DG)
# 		plt.figure()
# 		plt.axis('off')
# 		nx.draw_networkx(DG,pos=pos,with_labels=True)
# 		plt.show()

def frinds(DG, l):
    with open(r'C:\Users\hcx812591452\Desktop\facebook\3980.circles') as file_edge:
        lines = file_edge.readlines()
    # 真实划分的社区  格式：  {'1':['21','11'],'2':['23','31']}
    circle_edg = {}
    print(lines)
    for line in lines:
        data = line.split()
        circle_edg[re.sub("\D", "", data[0])] = list(data[1:])
    # 真实社区的总节点  格式：['21','11','23','31']
    frinds1 = []
    for key, values in circle_edg.items():
        for i in values:
            frinds1.append(int(i))
    # 连接社区的总节点数
    frinds = [int(i) for i in DG.neighbors(l)]
    # 真实社区和连接社区的共同节点
    frinds2 = sorted(list(set(frinds) & set(frinds1)))
    #  将friends 表示成['1','0','2']形式    表示节点属于的对应的社区
    frinds3 = frinds2[:]
    for key, values in circle_edg.items():
        for i in frinds3:
            if str(i) in values:
                frinds3[frinds3.index(i)] = int(key)
    return frinds2, frinds3


if __name__ == '__main__':
    DG, l = edges()
    frinds2, frinds3 = frinds(DG, l)
    print(frinds2)
    print(frinds3)
    '''
    #  链接社区划分
    s_matix = np.array(face.similarity_matix(DG.edges(), DG.number_of_edges(), DG))
    clusters, ave_density_list = face.clustering(s_matix, DG.edges(), 0)  # 聚为一个类，得到最大分区密度
    max_density = max(ave_density_list)
    clusters2, ave_density_list = face.clustering(s_matix, DG.edges(), max_density)  # 根据最大分区密度聚类
    print(clusters2)
    '''
    # 将边显示属于哪个社区
    # clusters3, clusters4 = DG.edges()
    # for i in list(DG.edges()):
    # 	for j in list(clusters2):
    # 		if i in j:
    # 			clusters3[clusters3.index(i)] = list(clusters2).index(j)+1
    '''
    color = []
    for c in seaborn.xkcd_rgb.values():  # 含有颜色的字典
        color.append(c)
    
    p = 0
    for	n in circle_edg.values():
        nx.draw_networkx_nodes(DG, pos=pos, nodelist=list(n), node_size=100,node_color=color[p])
        nx.draw_networkx_labels(DG, pos=pos,font_size=12)
        p += 4
    nx.draw_networkx_edges(DG, pos=pos, edgelist=DG.edges())
    plt.show()
    
    '''
    # import networkx as nx
    # import matplotlib.pyplot as plt
    # import numpy as np
    # with open(r'C:\Users\hcx812591452\Desktop\facebook\698.edges') as file_edge:
    # 	lines = file_edge.readlines()
    # edgeslist = []
    # lineeee = ''
    # for line in lines:
    # 	lineeee += line.rstrip()
    # for line in lineeee:
    # 	edg = (698, line)
    # 	edgeslist.append(edg)
    # print(list(set(edgeslist)))
    #
    # # with open(r"H:\新建文件夹 (2)\PycharmProjects\Test_9\facebook_combined.txt") as file_edge:
    # # 	line = file_edge.read()
    # # 	print(type(line))
    # 0  107  348  414  686  698  1684  1912  3437  3980
    # # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\0.edges", create_using=nx.Graph())
    # # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\348.edges", create_using=nx.Graph())
    # # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\414.edges", create_using=nx.Graph())
    # # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\686.edges", create_using=nx.Graph())
    # # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\3437.edges", create_using=nx.Graph())
    # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\3980.edges", create_using=nx.Graph())
    # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\1912.edges", create_using=nx.Graph())
    # # fb = nx.read_edgelist(r"C:\Users\hcx812591452\Desktop\facebook\698.edges", create_using=nx.Graph())
    # # pos = nx.spring_layout(fb)
    # # plt.figure()
    # # plt.axis('off')
    # # nx.draw_networkx(fb, pos=pos, with_labels=True, node_size=20)
    # # plt.show()
