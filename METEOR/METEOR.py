from konlpy.tag import Kkma

kkma = Kkma()


filename1 = 'Machine translation filename'  #Machine translation
filename2 = 'reference translation filename'  #reference translation
n = []
q = []

n1 = []
m1 = []

p1 = []
q1 = []

s = ""
r = ""

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
##############################################################################
count1 = []             #unigram List
for i in range(len(n)):
    cnt1 = 0
    for j in range(len(n[i])):
        etclist = []
        for k in range(len(q[i])):
            if n[i][j] == q[i][k]:
                if n[i][j] not in etclist:
                    etclist.append(n[i][j])
                    cnt1 += 1
    count1.append(cnt1)
##############################################################################
train_idx = list()
test_idx = list()

for stc_idx, n_sentence in enumerate(n):
   n_list = []
   q_list = []
   for n_idx, n_word in enumerate(n_sentence):
      for q_idx, q_word in enumerate(q[stc_idx]):
         if n_word == q_word:
            if n_idx in n_list or q_idx in q_list:
               pass
            else:
               n_list.append(n_idx)
               q_list.append(q_idx)

   train_idx.append(n_list)
   test_idx.append(q_list)

absolute = []               #Chunk List

for stc_idx, train_sentence in enumerate(train_idx):
   a = 0
   b = 0
   d = ''
   stc_list = []
   for w_idx in range(len(train_sentence) - 1):
      if train_idx[stc_idx][w_idx]+1 == train_idx[stc_idx][w_idx+1]:
         if a == 0:
            a = train_idx[stc_idx][w_idx]
            d += n[stc_idx][a]
            a += 1

         b = train_idx[stc_idx][w_idx+1]
         d += ' ' + n[stc_idx][b]
      else:
         if n[stc_idx][train_idx[stc_idx][w_idx]] in d:
            a = 0
            stc_list.append(d)
            d = ''
            continue
         else:
            a = 0
            stc_list.append(n[stc_idx][train_idx[stc_idx][w_idx]])
   stc_list.append(d)
   absolute.append(stc_list)
###########################################################################
P = []      #Precision
R = []      #Recall
Fmean = []      #Fmean
for a, i in enumerate(n):
    if len(i) == 0:
        P.append(0)
        R.append(0)
        continue
    elif len(q[a]) == 0:
        P.append(0)
        R.append(0)
        continue
    P_c = count1[a]/len(q[a])
    P.append(P_c)
    R_c = count1[a]/len(i)
    R.append(R_c)

for a in range(len(P)):
    if 9*P[a]+R[a] == 0:
        Fmean.append(0)
        continue
    F_c = (10*P[a]*R[a])/(9*P[a]+R[a])
    Fmean.append(F_c)

penalty = []
Score = []
total = 0
chunk = []
for i in range(len(absolute)):
    chunk.append(len(absolute[i]))

for i in range(len(n)):
    if count1[i] < 2:           #penalty의 계산에서 count1[i]가 2미만이면 분모가 0이되므로 count1[i]<2  , 다른 식을 참조할 때는 count1[i]<1
        penalty.append(1)           #if문 조건이 unigram이 없다는 조건이므로 penalty를 1로 줌
        continue
    p_1 = 0.5*((1.0*(chunk[i]-1)/(count1[i]-1)))**3     #p_1 = 0.5*((1.0*(chunk[i])/(count1[i])))**3   다른 식
    penalty.append(p_1)

for i in range(len(n)):
    ad = Fmean[i]*(1-penalty[i])
    Score.append(ad)

for i in range(len(Score)):
    total += Score[i]

METEOR = total/len(Score)   #METEOR 스코어
t = str(round(METEOR,4))+' '
print(t[2:4]+'.'+t[4:])     #METEOR 백분위
print(Score)                #각 문장들의 METEOR 값
