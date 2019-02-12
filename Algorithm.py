import sys
import random
from functions import *

#inisiasi global variabel
deck=[]

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
	(List,totalscore)=Listprocessf(List,totalscore)
	totalscore-=abs(24-List[0].N)
	fx = open(sys.argv[2],"w")#tulis ke file
	fx.write(List[0].E)
	fx.write("\nTotal Skor: ")
	fx.write(str(totalscore))

if (len(sys.argv) == 3):
	mainwithargv()
else:
	print("--------------- ERROR ---------------")
	if (len(sys.argv) == 2):
		print("      Output file not initiated")
	elif (len(sys.argv) == 1):
		print(" Input and output file not initiated")
