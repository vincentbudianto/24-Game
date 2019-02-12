import sys
import random
from Classes import Numbers,card

#inisiasi global variabel
List=[]
filedir="./Picture/"
fileext=".png"
suit=["S","D","C","H"]
specialcard=["A","J","Q","K"]
totalscore=0

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
	return deck

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
'''
with open(sys.argv[1],"r") as f:
	#read first line
	data = [int(value) for value in next(f).split()]
	#case > 1 line
	# array = [[int(value) for value in line.split()] for line in f]
	# print (data)
'''
def partition(data,low,high):
	i = (low - 1)   #index
	pivot = data[high]

	for j in range(low,high):
		#jika nilai sekarang > dari tumpuan
		if data[j] > pivot:
			i = i + 1
			data[i],data[j] = data[j],data[i]

	data[i+1],data[high] = data[high],data[i+1]
	return (i + 1)

def draw4(deck):  #mengambil 4 kartu dari deck (fungsi)
	global List
	List=[]
	drawncards=[]
	
	for i in range (1,5):
		x=random.randint(0,len(deck)-1)
		c=deck.pop(x)
		drawncards.append(c)
		List.append(c.c2n())
	return (List,deck,drawncards)
	
def Listprocessf(List,totalscore):
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
	return (List,totalscore)

def quickSort (data,low,high):
	if low < high:
		pi = partition(data,low,high)

		quickSort(data,low, pi-1)
		quickSort(data,pi+1, high)
'''
n = len(data)
quickSort(data,0,n-1)
print (data)
'''
