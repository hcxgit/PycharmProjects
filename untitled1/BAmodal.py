#coding:utf-8
import networkx as nx
import matplotlib.pyplot as plt

def barabasi_albert_graph(n, m):
    # 生成一个包含m个节点的空图 (即BA模型中t=0时的m0个节点)
    G=empty_graph(m)
    # 定义新加入边要连接的m个目标节点
    targets=range(m)
    # 将现有节点按正比于其度的次数加入到一个数组中，初始化时的m个节点度均为0，所以数组为空
    repeated_nodes=[]
    # 添加其余的 n-m 个节点，第一个节点编号为m（Python的数组编号从0开始）
    source=m
    # 循环添加节点
    while source<n:
        # 从源节点连接m条边到选定的m个节点targets上（注意targets是上一步生成的）
        G.add_edges_from(zip([source]*m,targets))
        # 对于每个被选择的节点，将它们加入到repeated_nodes数组中（它们的度增加了1）
        repeated_nodes.extend(targets)
        # 将源点m次加入到repeated_nodes数组中（它的度增加了m）
        repeated_nodes.extend([source]*m)
        # 从现有节点中选取m个节点 ，按正比于度的概率（即度优先连接）
        targets=set()
        while len(targets)<m:
            #按正比于度的概率随机选择一个节点，见注释1
            x=random.choice(repeated_nodes)
            #将其添加到目标节点数组targets中
            targets.add(x)
        #挑选下一个源点，转到循环开始，直到达到给定的节点数n
        source += 1
    #返回所得的图G
    return G