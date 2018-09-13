# -*- coding: utf-8 -*-

'''
import networkx as nx
import matplotlib.pyplot as plt
# BA scale-free degree network
# generalize BA network which has 20 nodes, m = 1
BA = nx.random_graphs.barabasi_albert_graph(5, 1)
# spring layout
pos = nx.circular_layout(BA)
nx.draw(BA, pos, with_labels = False, node_size = 30)
plt.show()
'''

""" 
An example using Graph as a weighted network. 
"""
__author__ = """Aric Hagberg (hagberg@lanl.gov)"""
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()
# 添加带权边
G.add_edges_from([('S','B'),('S','C'),('S','D'),('E','F'),('D','C'),('S','E'),('S','F'),('B','G'),('B','G'),('B','H'),('C','H'),('D','I'),('D','J'),
	('E','K'),('E','L'),('F','M'),('F','G')])

# G.add_edge('s', 'b', weight=0.6)
# G.add_edge('s', 'c', weight=0.4)
# G.add_edge('s', 'd', weight=0.4)
# G.add_edge('s', 'e', weight=0.4)
# G.add_edge('s', 'f', weight=0.4)
# 节点位置
# pos = nx.circular_layout(G)
# 首先画出节点位置
# nodes
# nx.draw_networkx_nodes(G, pos, node_size=700)
# 根据权重，实线为权值大的边，虚线为权值小的边
# edges
# nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
# nx.draw_networkx_edges(G, pos, edgelist=esmall,width=6, alpha=0.5, edge_color='b', style='dashed')

# labels标签定义
# nx.draw_networkx_edges(G, pos, width=6,style='dashed')
# nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')
nx.draw(G,with_labels=True, font_weight='bold')
# nx.draw_shell(G,nlist = [['S'],[('S','B'),('S','C'),('S','D'),('E','F'),('D','C'),('S','E'),('S','F')],[('B','G'),('B','G'),('B','H'),('C','H'),('D','I'),('D','J'),
# 	('E','K'),('E','L'),('F','M'),('F','G')]],with_labels=True)
plt.axis('off')
plt.savefig("weighted_graph.png")  # save as png
plt.show()  # display