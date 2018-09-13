# -*- coding:utf-8 -*-
'''

@summary: 利用Python实现NMI计算

'''
import math
import numpy as np
from sklearn import metrics
def	NMI(A, B):
    # 样本点数
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    # 互信息计算
    MI = 0
    eps = 1.4e-45
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = np.where(A == idA)
            idBOccur = np.where(B == idB)
            idABOccur = np.intersect1d(idAOccur,idBOccur)  # A B公共元素
            px = 1.0*len(idAOccur[0])/total
            py = 1.0*len(idBOccur[0])/total
            pxy = 1.0*len(idABOccur)/total
            MI = MI + pxy*np.log2(pxy/(px*py)+eps)
    # 标准化互信息
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0*len(np.where(A == idA)[0])
        Hx = Hx - (idAOccurCount/total)*np.log2(idAOccurCount/total+eps)
    Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0*len(np.where(B == idB)[0])
        Hy = Hy - (idBOccurCount/total)*np.log2(idBOccurCount/total+eps)
    MIhat = 2.0*MI/(Hx+Hy)
    return MIhat

if __name__ == '__main__':
    A = np.array([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3])
    B = np.array([1,2,1,4,1,2,1,2,3,2,4,3,1,1,3,3,4])
    print (NMI(A, B))
    print (metrics.normalized_mutual_info_score(A, B))
    # a = np.array([[('1','2'),('3','5')],
    #      [('2','3'),('5','6')],
    #      [('4','5'),('6','7'),('8','9')]])
    # print(a)
    # b=0
    # max_len = 0
    # index = 0
    # for i in a:
    #     lens = len(a[index])
    #     for j in i:
    #         if str(5) in j:
    #             if lens >= max_len:
    #                 b = index
    #                 max_len = lens
    #     index += 1
    # print(b)