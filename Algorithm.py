import sys
import random
from functions import *

#inisiasi global variabel
deck=[]

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
    (List[0].E,totalscore)=kurung(List[0].E,totalscore)
    fx = open(sys.argv[2],"w")#tulis ke file
    fx.write(List[0].E)
    fx.write("\nTotal Skor: ")
    fx.write(str(int(totalscore)))

if (len(sys.argv) == 3):
	mainwithargv()
else:
	print("--------------- ERROR ---------------")
	if (len(sys.argv) == 2):
		print("      Output file not initiated")
	elif (len(sys.argv) == 1):
		print(" Input and output file not initiated")
