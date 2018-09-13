import math

# with open(r'C:\Users\hcx812591452\Desktop\数据集\facebook\698.feat') as file_edge:  ##262310943   532617990
#     lines = file_edge.readlines()
#     s = [[0 for i in range(len(lines)+1)] for i in range(len(lines)+1)]
#     for l in lines:
#         index1 = lines.index(l)
#         l = l.split()
#         s[index1+1][0]=l[0]
#         s[0][index1+1]=l[0]
#         for l2 in lines:
#             index2 = lines.index(l2)
#             number =0
#             l2 = l2.split()
#             for i in range(len(l2)-1):
#                 if l[i+1] != l2[i+1]:
#                     number += 1
#             s[index1+1][index2+1] = 1/math.exp(number)
#     print(s)
#     print(s[s[:][0].index(str(810))][:])
def feat():
    with open(r'C:\Users\hcx812591452\Desktop\数据集\facebook\698.feat') as file_edge:  ##262310943   532617990
        lines = file_edge.readlines()
        s = [[0 for i in range(len(lines[0].split()))] for i in range(len(lines)+1)]
        for l in lines:
            index1 = lines.index(l)
            l = l.split()
            s[index1]=l
            # s[0][index1+1]=l[0]
    with open(r'C:\Users\hcx812591452\Desktop\数据集\facebook\698.egofeat') as f:
        lines2 = f.readlines()
        s[len(lines)][0]=str(698)
        s[len(lines)][1:]=lines2[0].split()
        return s
def similarity2(i1,i2,i3,i4,s):
    for i in range(len(s)):
        if s[i][0]==i1:
            s1 = s[i]
        if s[i][0]==i2:
            s2 = s[i]
        if s[i][0]==i3:
            s3 = s[i]
        if s[i][0]==i4:
            s4 = s[i]
    s12 = [0 for i in range(len(s1)-1)]
    s34 = [0 for i in range(len(s1)-1)]
    for j in range(len(s1)-1):
        if s1[j+1]==str(1) or s2[j+1]==str(1):
            s12[j]=1
        if s3[j+1]==str(1) or s4[j+1]==str(1):
            s34[j]=1
    # del s1, s2, s3, s4
    number = 0
    for i in range(len(s12)):
        if s12[i] == s34[i]==1:
            number += 1
    print(s)
    print(s1)
    print(s2)
    print(s12)
    print(s34)
    print(len(s12))
    print(len(s34))
    print(number/len(s12))
if __name__ == '__main__':
    similarity2(str(861),str(698),str(698),str(873),feat())