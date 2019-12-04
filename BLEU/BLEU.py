import math
from konlpy.tag import Kkma

kkma = Kkma()

filename1 = 'Machine translation filename'  #Machine translation
filename2 = 'reference translation filename'  #reference translation

count1 = []
count2 = []
count3 = []
count4 = []

m = []
m1 = []
n = []
n1 = []

s = ""

p = []
p1 = []
q = []
q1 = []
r = ""

t = ""
#############################################################################
with open(filename1, 'r') as f:
    for sentence in f:
        s += sentence
m = s.split('\n')

for i in m:
    n1.append(kkma.pos(i))
for i in m:
    m1.append(kkma.morphs(i))
for i in range(len(n1)):
    for j in range(len(n1[i])):
        m1[i][j] = [n1[i][j][0], n1[i][j][1]]
        if m1[i][j][1] == 'EFN':
            m1[i][j][0] = '다'
        if m1[i][j][0] == '?':
            if m1[i][j-1][1] == 'EFQ':
                m1[i][j-1][0] = '까'
for i in range(len(m1)):
    for j in range(len(m1[i])):
         m1[i][j] = m1[i][j][0]
n = m1

#############################################################################
with open(filename2, 'r') as f:
    for sentence in f:
        r += sentence
p = r.split('\n')
for i in p:
    q1.append(kkma.pos(i))
for i in p:
    p1.append(kkma.morphs(i))
for i in range(len(q1)):
    for j in range(len(q1[i])):
        p1[i][j] = [q1[i][j][0], q1[i][j][1]]
        if p1[i][j][1] == 'EFN':
            p1[i][j][0] = '다'
        if p1[i][j][0] == '?':
            if p1[i][j-1][1] == 'EFQ':
                p1[i][j-1][0] = '까'
for i in range(len(p1)):
    for j in range(len(p1[i])):
         p1[i][j] = p1[i][j][0]
q = p1
#############################################################################
n2 = []
n3 = []
n4 = []
q2 = []
q3 = []
q4 = []
for z1 in range(len(n)):
    n2.append("")
    n3.append("")
    n4.append("")
for z2 in range(len(q)):
    q2.append("")
    q3.append("")
    q4.append("")
#############################################################################
for e in range(len(n)):
    g1 = 0
    for e1 in range(len(n[e])):
        g1 += 1
    if len(n[e]) > 1:
        n2[e] = []*(g1-1)
    if len(n[e]) > 2:
        n3[e] = []*(g1-2)
    if len(n[e]) > 3:
        n4[e] = []*(g1-3)
#############################################################################
for f in range(len(q)):
    g1 = 0
    for f1 in range(len(q[f])):
        g1 += 1
    if len(q[f]) > 1:
        q2[f] = []*(g1-1)

    if len(q[f]) > 2:
        q3[f] = []*(g1-2)

    if len(q[f]) > 3:
        q4[f] = []*(g1-3)

#############################################################################
for i in range(len(n)):
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    cnt4 = 0
    for k1_1 in range(len(n[i])):
        etclist = []
        for k1_2 in range(len(q[i])):
            if n[i][k1_1] == q[i][k1_2]:
                if n[i][k1_1] not in etclist:
                    etclist.append(n[i][k1_1])
                    cnt1 += 1
    count1.append(cnt1)
#############################################################################
    if len(n[i])>1 and len(q[i])>1:
        for k2_1 in range(len(n[i])-1):
            t = n[i][k2_1]+' '+n[i][k2_1+1]
            n2[i].append(t)
        for k2_2 in range(len(q[i])-1):
            t = q[i][k2_2]+' '+q[i][k2_2+1]
            q2[i].append(t)
        for k2_3 in range(len(n2[i])):
            etclist = []
            for k2_4 in range(len(q2[i])):
                if n2[i][k2_3] == q2[i][k2_4]:
                    if n2[i][k2_3] not in etclist:
                        etclist.append(n2[i][k2_3])
                        cnt2 += 1
    count2.append(cnt2)
#############################################################################
    if len(n[i])>2 and len(q[i])>2:
        for k3_1 in range(len(n[i])-2):
            t = n[i][k3_1]+' '+n[i][k3_1+1]+' '+n[i][k3_1+2]
            n3[i].append(t)
        for k3_2 in range(len(q[i])-2):
            t = q[i][k3_2]+' '+q[i][k3_2+1]+' '+q[i][k3_2+2]
            q3[i].append(t)
        for k3_3 in range(len(n3[i])):
            etclist = []
            for k3_4 in range(len(q3[i])):
                if n3[i][k3_3] == q3[i][k3_4]:
                    if n3[i][k3_3] not in etclist:
                        etclist.append(n3[i][k3_3])
                        cnt3 += 1
    count3.append(cnt3)
#############################################################################
    if len(n[i])>3 and len(q[i])>3:
        for k4_1 in range(len(n[i])-3):
            t = n[i][k4_1]+' '+n[i][k4_1+1]+' '+n[i][k4_1+2]+' '+n[i][k4_1+3]
            n4[i].append(t)
        for k4_2 in range(len(q[i])-3):
            t = q[i][k4_2]+' '+q[i][k4_2+1]+' '+q[i][k4_2+2]+' '+q[i][k4_2+3]
            q4[i].append(t)
        for k4_3 in range(len(n4[i])):
            etclist = []
            for k4_4 in range(len(q4[i])):
                if n4[i][k4_3] == q4[i][k4_4]:
                    if n4[i][k4_3] not in etclist:
                        etclist.append(n4[i][k4_3])
                        cnt4 += 1
    count4.append(cnt4)
#############################################################################
leng1 = []
leng2 = []
for i in range(len(n)):
    recount1 = 0
    recount2 = 0
    for j in range(len(n[i])):
        recount1 += 1
    leng1.append(recount1)
    for k in range(len(q[i])):
        recount2 += 1
    leng2.append(recount2)
cal = []
for i in range(len(leng1)):
    if leng1[i] < 4:
        cal.append(0)
        continue
    elif leng2[i] == 0:
        cal.append(0)
    else:
        b = (1.0*count1[i]/leng1[i]*count2[i]/(leng1[i]-1)*count3[i]/(leng1[i]-2)*count4[i]/(leng1[i]-3))  #unigram ~ quadrigram precision
        b = math.sqrt(b)
        b = math.sqrt(b)
        cal.append(b)
cn = 0
for i in range(len(cal)):
    cn += cal[i]
refer_leng = 0
candi_leng = 0
for i in range(len(n)):
    candi_leng += len(n[i])
    refer_leng += len(q[i])

length = 0

if candi_leng > refer_leng:
    length = 1
else:
    length = candi_leng/refer_leng

BLEU = cn/len(cal)*length   #전체 문장들의 BLEU Score 0을 포함한 평균 BLEU 값
t = str(round(BLEU,4))+' '
print(t[2:4]+'.'+t[4:])    #전체 문장들의 BLEU Score 0을 포함한 평균 BLEU 백분위

####################################################################

final_score = []
for i in range(len(cal)):
    final_score.append(cal[i]*len(n[i])/len(q[i]))
final_list = []
for j in range(len(cal)):
    if final_score[j] > 0:
        final_list.append(final_score[j])
print("각 문장 BLEU : ", final_list) #BLEU Score 0을 포함하지 않은 각 문장들의 BLEU 값
print("평균 : ", sum(final_list)/len(final_list))  #BLEU Score 0을 포함하지 않은 각 문장들의 BLEU 평균값