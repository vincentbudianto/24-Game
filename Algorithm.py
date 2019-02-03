#Algorithm.py = file untuk algoritma

from main import partition,quickSort
from Classes import Numbers

#inisiasi global variabel
List=[]
totalscore=0

#fungsi tambahan
def compare24(num,exp): #menghitung bobot skor
    skor=0
    if (exp=='+'):
        skor+=5
    if (exp=='-'):
        skor+=4
    if (exp=='*'):
        skor+=3
    if (exp=='/'):
        skor+=2
    skor=skor-abs(24-num)
    return skor

def main(): #main program
    global List
    global totalscore
    with open("case.txt","r") as f: #baca teks dari hans
        #read first line
        for value in next(f).split():
            value=int(value)
            x=Numbers(value,str(value))
            List.append(x)
    quickSort(List,0,len(List)-1)
    while (len(List)>1):
        N1=List.pop(0)
        N2=List.pop(0)
        if (N1<=24):
            if (compare24(N1+N2,'+')>compare24(N1*N2,'*')):
                N3=N1.operate('+',N2)
                totalscore+=5
            else:
                N3=N1.operate('*',N2)
                totalscore+=3
        else:
            if (compare24(N1-N2,'-')>compare24(N1/N2,'/')):
                N3=N1.operate('-',N2)
                totalscore+=4
            else:
                N3=N1.operate('/',N2)
                totalscore+=2
        List.append(N3)
        quickSort(List,0,len(List)-1)
    print(List[0].E)
    totalscore-=abs(24-List[0].N)
    print("totalscore="+str(totalscore))

main()
