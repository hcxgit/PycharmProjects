# coding:utf-8
# from pylab import mpl
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy.cluster.hierarchy as sch
from collections import defaultdict
import sys
import seaborn
import gc
from sklearn import metrics
import re
sys.setrecursionlimit(100000)
# import edges
# mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
# mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


# 边相似度计算
def similarity(i, j, k, DG):
    j_neighbors = list(DG.neighbors(j))  # j 的所有邻居
    j_neighbors.append(j)  # 包含j
    k_neighbors = list(DG.neighbors(k))  # k 的所有邻居
    k_neighbors.append(k)
    j_and_k = set(j_neighbors) & set(k_neighbors)  # 交集
    j_or_k = set(j_neighbors) | set(k_neighbors)  # 并集
    S = float(len(j_and_k)) / len(j_or_k)
    return S


#  相似度矩阵
def similarity_matix(edges, longth_edges, DG):
    # 相似度矩阵   第0行和第0列表示类的代号
    # s_matix = np.zeros((longth_edges+1, longth_edges+1))
    s_matix = [[0 for i in range(longth_edges + 1)] for i in range(longth_edges + 1)]
    for i in range(1, len(s_matix)):
        s_matix[0][i] = i - 1
        s_matix[i][0] = i - 1
    i = 1
    for x in edges:
        j = 1
        for y in edges:
            # 同边
            if x == y:
                s_matix[i][j] = 1
            # 有共同点
            elif x[0] == y[0]:
                s_matix[i][j] = similarity(x[0], x[1], y[1], DG)+similarity2(x[1],y[1])
            elif x[0] == y[1]:
                s_matix[i][j] = similarity(x[0], x[1], y[0], DG)+similarity2(x[1],y[0])
            elif x[1] == y[0]:
                s_matix[i][j] = similarity(x[1], x[0], y[1], DG)+similarity2(x[0],y[1])
            elif x[1] == y[1]:
                s_matix[i][j] = similarity(x[1], x[0], y[0], DG)+similarity2(x[0],[0])
            # 没有共同点
            else:
                s_matix[i][j] = 0
            j += 1
        i += 1
    return s_matix
def similarity2(i, j):
    with open(r'C:\Users\hcx812591452\Desktop\数据集\twitter\262310943.feat') as file_edge:
        lines = file_edge.readlines()
        for l in lines:
            if i==l[0]:
                i_1=lines.index(l)
            if j == l[0]:
                j_1 = lines.index(l)
        number =0
        for i in lines[i_1]:
            for j in lines[j_1]:
                if i ==j:
                    number =1
        return 1/len(lines)

# 用最近邻方法合并类，更新矩阵
def distances(a, b, c, s_matix):
    for i in range(1, len(s_matix)):
        s_matix[a][i] = s_matix[i][a] = max(s_matix[a][i], s_matix[b][i])  # a、b的内容取值放入a
    s_matix[a][0] = s_matix[0][a] = c  # 类代号改变
    s_matix = np.delete(s_matix, b, axis=0)  # 删除b
    s_matix = np.delete(s_matix, b, axis=1)
    return s_matix


# 分区密度  m：边数，n：点数
def density(m, n):
    try:
        return 2 * (m - n + 1.0) / (n - 2.0) / (n - 1.0)
    except ZeroDivisionError:  # 分母为0
        return 0.0


# 平均分区密度
def ave_Density(density_list, edges, clusters):
    sum = 0
    for i, element in enumerate(density_list):
        sum += element * len(clusters[i])
    return sum / len(edges)


# 聚类函数
def clustering(s_matix, edges, max_density):
    clusters = [[0 for col in range(0, len(s_matix) - 1)] for row in range(0, len(s_matix) - 1)]  # 初始化n个类
    # HC = []          			 		 			# 用来和树状图对接
    density_list = []  # 分区密度列表
    for i in range(0, len(s_matix) - 1):  # 初始化聚类列表和分区密度列表
        clusters[i] = [x for x in list(edges)[i]]
        density_list.append(density(1, 2))
    ave_density_list = []  # 平均分区密度列表
    ave_density_list.append(ave_Density(density_list, edges, clusters))

    num_clusters = len(s_matix) - 1  # 合并类的代号
    if max_density == 0:  # 标志位   传进来的max_density 为0，则聚类为一个  否则按照max_density聚类
        while len(clusters) > 1:  # 判断聚类是否完成
            max_similar = 0
            point1 = 1
            point2 = 1
            for i in range(1, len(s_matix) - 1):
                for j in range(i + 1, len(s_matix)):
                    if s_matix[i][j] >= max_similar:
                        max_similar = s_matix[i][j]
                        point1 = i
                        point2 = j
                    else:
                        continue

            for c in clusters[point2 - 1]:  # 将合并的类归入
                clusters[point1 - 1].append(c)

            del density_list[point2 - 1]  # 更新density_list
            density_list[point1 - 1] = density(len(clusters[point1 - 1]), len(list(np.unique(clusters[point1 - 1]))))
            ave_density_list.append(ave_Density(density_list, edges, clusters))  # 更新ave_density_list

            # hc = [s_matix[0][point1], s_matix[0][point2], max_similar, len(clusters[point1-1])]
            # HC.append(hc)
            s_matix = distances(point1, point2, num_clusters, s_matix)  # 合成相似度最大的两个类,改变矩阵
            clusters = np.delete(clusters, point2 - 1, axis=0)  # 类的总数减少了一个
            num_clusters += 1
        # c.collect()
    else:
        max_similar = 1
        while max_similar >= max_density:  # 判断聚类是否完成
            max_similar = 0
            point1 = 1
            point2 = 1
            for i in range(1, len(s_matix) - 1):
                for j in range(i + 1, len(s_matix)):
                    if s_matix[i][j] >= max_similar:
                        max_similar = s_matix[i][j]
                        point1 = i
                        point2 = j
                    else:
                        continue

            for c in clusters[point2 - 1]:  # 将合并的类归入
                clusters[point1 - 1].append(c)

            del density_list[point2 - 1]  # 更新density_list
            density_list[point1 - 1] = density(len(clusters[point1 - 1]), len(list(np.unique(clusters[point1 - 1]))))
            ave_density_list.append(ave_Density(density_list, edges, clusters))  # 更新ave_density_list

            # hc = [s_matix[0][point1], s_matix[0][point2], max_similar, len(clusters[point1 - 1])]
            # HC.append(hc)
            s_matix = distances(point1, point2, num_clusters, s_matix)  # 合成相似度最大的两个类,改变矩阵
            clusters = np.delete(clusters, point2 - 1, axis=0)  # 类的总数减少了一个
            num_clusters += 1
    return clusters, ave_density_list


def ego_graph():
    #  获取边列表
    fb = nx.read_edgelist(r"D:\新建文件夹 (2)\PycharmProjects\Test_9\twitter_combined.txt", create_using=nx.Graph())
    # 获取ego节点并画出图
    # print (nx.info(fb))
    print('输入节点的值，并显示节点对应的ego网络图')
    ego_me = input()

    # # 读爬取的数据
    # with open(r'H:\新建文件夹 (2)\PycharmProjects\AppSpider\circle_edges1.txt', 'r') as file:
    #     f = eval(file.readline())
    # circle_edgess = []  # 存储 边
    # ego_me = '带拉格朗日余项的平衡二叉树'
    # for k, v in f.items():
    #     for vs in list(v):
    #         if k.lstrip() != vs.lstrip():
    #             circle_edgess.append((k.lstrip(), vs.lstrip()))  # 加入发表人和点赞人的边
    #             if vs.lstrip() != ego_me:
    #                 circle_edgess.append((ego_me, vs.lstrip()))  # 加入ego节点和点赞人的边
    #         if k.lstrip() != ego_me:
    #             circle_edgess.append((ego_me, k))  # 加入ego节点和发表人的边
    # circle_edgess = list(set(circle_edgess))
    # print(circle_edgess)
    # 将数据整理成ego网络
    # fb = nx.Graph()
    # fb.add_edges_from(circle_edgess)

    if ego_me in fb.nodes():
        node_ego = nx.ego_graph(fb, ego_me)
        dg = nx.Graph(node_ego)
        pos = nx.spring_layout(dg)
        plt.figure()
        plt.axis('off')
        nx.draw_networkx(dg, pos=pos, with_labels=True)
        plt.show()
        return dg


# 真实社区
def edges():
    fb = nx.read_edgelist(r"D:\新建文件夹 (2)\PycharmProjects\Test_9\facebook_combined.txt", create_using=nx.Graph())
    r_l = '348'
    if r_l in fb.nodes():
        node_ego = nx.ego_graph(fb, r_l)  # 自我中心节点
        r_DG = nx.Graph(node_ego)  # 节点l的ego网络图
        return r_DG, r_l


# 将真实社区以每个节点所属社区的形式表示
def frinds(r_DG, r_l):
    with open(r'C:\Users\hcx812591452\Desktop\facebook\348.circles') as file_edge:
        lines = file_edge.readlines()
    # 真实划分的社区  格式：  {'1':['21','11'],'2':['23','31']}
    circle_edg = {}
    for line in lines:
        data = line.split()
        circle_edg[re.sub("\D", "", data[0])] = list(data[1:])
    # 真实社区的总节点  格式：['21','11','23','31']
    frinds1 = []
    for key, values in circle_edg.items():
        for i in values:
            frinds1.append(int(i))
    # 连接社区的总节点数
    frinds = [int(i) for i in r_DG.neighbors(r_l)]
    # 真实社区和连接社区的共同节点
    frinds2 = sorted(list(set(frinds) & set(frinds1)))
    #  将friends 表示成['1','0','2']形式    表示节点属于的对应的社区
    frinds3 = frinds2[:]
    for key, values in circle_edg.items():
        for i in frinds3:
            if str(i) in values:
                frinds3[frinds3.index(i)] = int(key)
    print(frinds2)
    return frinds2, frinds3


# 将划分的社区以每个节点所属社区的形式表示
def node_circle(clusters2, frinds):
    frinds2 = frinds[:]
    for f in frinds:
        id = 0  # 社区id
        min_len = len(frinds)  # 每个节点所属最大社区的长度
        for i in list(clusters2):
            lens = len(clusters2[id])
            for j in i:
                if str(f) in j:
                    if lens <= min_len:
                        frinds2[frinds.index(f)] = id
                        min_len = lens
                    break
            id += 1
    return frinds2

'''
    ##  格式
def frinds(DG):
    # 真实社区的总节点  0高中 1本科 2家人 3朋友 4研究生 5初中 6现在班级
    frinds = sorted(['陈灿', '余生', '小ｖ', '双手合十亦步亦趋', '姐姐', 'YUAN', '吴小胖', 'Shaun', '郭文娜',
                     '蒙', 'i want', 'A张新新', '暖阳', '张倩', '贺自信', '嘿嘿', '泰宁先生', '王豪18661847581'])
    frinds1 = [0, 4, 2, 0, 0, 1, 3, 4, 2, 1, 2, 5, 6, 6, 0, 6, 4, 0]
    return frinds, frinds1
'''


if __name__ == "__main__":

    DG = ego_graph()
    s_matix = np.array(similarity_matix(DG.edges(), DG.number_of_edges(), DG))
    print(s_matix)
    # ++++++++++++++++++++++++++++++++++
    clusters, ave_density_list = clustering(s_matix, DG.edges(), 0)  # 聚为一个类，得到最大分区密度

    #  分区密度画图
    '''
    plt.figure()
    plt.plot(ave_density_list)
    plt.ylabel("density")
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.show()
    '''

    # HC = np.array(HC)
    # print(HC)
    # print(ave_density_list)
    # sch.dendrogram(HC, color_threshold=1, truncate_mode='lastp', show_contracted=True,orientation='bottom')
    #  将层级聚类结果以树状图表示出来
    # sch.dendrogram(HC, color_threshold=1, truncate_mode='lastp')  # 将层级聚类结果以树状图表示出来
    # plt.gca().invert_yaxis()
    # plt.show()

    max_density = max(ave_density_list)
    print(max_density)
    clusters2, ave_density_list = clustering(s_matix, DG.edges(), max_density)  # 根据最大分区密度聚类
    print(clusters2)

    # # NMI
    # ego_me = '带拉格朗日余项的平衡二叉树'
    # frinds, frinds1 = frinds(DG)
    # print(frinds)
    # print(frinds1)

    t_DG, r_l = edges()  # 真实社区
    frinds2, frinds3 = frinds(t_DG,r_l)  # 共同节点、真实社区格式化后的节点
    frinds4 = node_circle(clusters2, frinds2)  # 链接社区格式化后的节点
    print(metrics.normalized_mutual_info_score(frinds3, frinds4))

    # 将边显示属于哪个社区
    '''
    clusters3, clusters4 = DG.edges()
    for i in list(DG.edges()):
        for j in list(clusters2):
            if i in j:
                clusters3[clusters3.index(i)] = list(clusters2).index(j)+1
    print(DG.edges())
    print(clusters3)
    '''
    # 画图
    #
    # clusters2 = list(clusters2)
    # p = 0
    # color = []
    # for c in seaborn.xkcd_rgb.values():  # 含有颜色的字典
    #     color.append(c)
    # pos = nx.spring_layout(DG)
    # for v in clusters2:
    #     for n in v:
    #         nx.draw_networkx_nodes(DG, pos=pos, nodelist=list(n), node_size=100)
    #         nx.draw_networkx_labels(DG, pos=pos, font_size=15)
    #     nx.draw_networkx_edges(DG, pos=pos, edgelist=v, edge_color=color[p])
    #     p += 1
    # plt.show()
