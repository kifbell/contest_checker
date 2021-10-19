cnts=dict()
with open('input.txt','r',encoding='utf8') as inpDescriptor:
    candidate=inpDescriptor.readline().rstrip()
    votecnt=0
    while candidate!='':
        cnts[candidate]=cnts.setdefault(candidate,0)+1
        votecnt+=1
        candidate=inpDescriptor.readline().rstrip()
maxInd1=''
maxInd2=''
for candidate in cnts:
    if maxInd1=='' or cnts[candidate]>cnts[maxInd1]:
        maxInd1,maxInd2=candidate,maxInd1
    elif maxInd2=='' or cnts[maxInd2]<cnts[candidate]:
        maxInd2=candidate
print(maxInd1)
if cnts[maxInd1]<=votecnt/2:
    print(maxInd2)
