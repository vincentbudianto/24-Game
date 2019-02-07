#Algorithm.py = file untuk algoritma

import sys
import random
from main import partition,quickSort
from Classes import Numbers,card

#inisiasi global variabel
deck=[]
List=[]
totalscore=0
filedir="./Picture/"
fileext=".png"
specialcard=["A","J","Q","K"]
suit=["S","D","C","H"]

#fungsi tambahan
def initiatedeck(): #inisiasi dek
    global deck
    deck=[]
    for i in range(1,14):
        for fn in suit:
            if (i==1 or i>10):
                s=filedir+specialcard[(i%10)+(i//10)-1]+fn+fileext
                c=card(i,s)
                deck.append(c)
            else:
                s=filedir+str(i)+fn+fileext
                c=card(i,s)
                deck.append(c)

def take4():  #mengambil 4 kartu dari deck
    global deck
    global List
    for i in range (1,5):
        x=random.randint(0,len(deck)-1)
        c=deck.pop(x)
        List.append(c.c2n())

def Listprocess():
    global List
    global totalscore
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

def kurung(st): #menambahkan kurung pada st
    global totalscore
    b=[]
    idx=[]
    i=0
    while (i<len(st)):
        ch=st[i]
        if (ch=='+') or (ch=='-'):
            b.append(False)
            idx.append(i)
        elif (ch=='/') or (ch=='*'):
            b.append(True)
            idx.append(i)
        i+=1
    if (not b[1] and b[2]):
        return "("+st[0:idx[2]]+")"+st[idx[2]:]
        totalscore-=1
    elif (not b[0] and b[1]):
        return "("+st[0:idx[1]]+")"+st[idx[1]:]
        totalscore-=1
    else:
        return st


def mainwithargv(): #main program
    global List
    global totalscore

    List=[]
    with open(sys.argv[1],"r") as f: #baca teks dari hans
        #read first line
        for value in next(f).split():
            value=int(value)
            x=Numbers(value,str(value))
            List.append(x)
    Listprocess()
    print(List[0].E)
    totalscore-=abs(24-List[0].N)
    print("totalscore="+str(totalscore))
    fx = open(sys.argv[1],"w")#tulis ke file
    fx.write(List[0].E)
    fx.write("\nTotal Skor: ")
    fx.write(str(totalscore))

def mainwithcards():
    global deck
    global List
    global totalscore
    List=[]
    take4()
    Listprocess()
    List[0].E=kurung(List[0].E)
    #print(s)
    totalscore-=abs(24-List[0].N)
    #print("totalscore="+str(totalscore))



if (len(sys.argv)>1):
    mainwithargv()
else:
    n24=0
    scoring=0
    for i in range (0,1000):
        totalscore=0
        initiatedeck()
        mainwithcards()
        if List[0].N == 24:
            n24+=1
        print(List[0].E)
        print(totalscore)
        scoring=scoring+totalscore
    print(n24)
    print(scoring/1000)
