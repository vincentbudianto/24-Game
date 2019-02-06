#File untuk kelas

class Numbers:
    """Numbers= Bagian dari list dari input number"""

    def __init__(self,number,expression): #ctor dengan 2 parameter
        self.N = number
        self.E = expression

    def operate(self,op,Nx):#fungsi merge 2 numbers
        if (op=='+'):
            Num=self.N+Nx.N
            Exp=self.E+"+"+Nx.E
        if (op=='-'):
            Num=self.N-Nx.N
            Exp=self.E+"-"+Nx.E
        if (op=='*'):
            Num=self.N*Nx.N
            Exp=self.E+"*"+Nx.E
        if (op=='/'):
            Num=self.N/Nx.N
            Exp=self.E+"/"+Nx.E
        NewN=Numbers(Num,Exp)
        return NewN

    #Operator overloading
    def __lt__(self,Nx):
        try:
            return (self.N<Nx.N)
        except AttributeError:
            return (self.N<Nx)
    def __le__(self,Nx):
        try:
            return (self.N<=Nx.N)
        except AttributeError:
            return (self.N<=Nx)
    def __eq__(self,Nx):
        try:
            return (self.N==Nx.N)
        except AttributeError:
            return (self.N==Nx)
    def __ne__(self,Nx):
        try:
            return (self.N!=Nx.N)
        except AttributeError:
            return (self.N!=Nx)
    def __gt__(self,Nx):
        try:
            return (self.N>Nx.N)
        except AttributeError:
            return (self.N>Nx)
    def __ge__(self,Nx):
        try:
            return (self.N>=Nx.N)
        except AttributeError:
            return (self.N>=Nx)
    def __add__(self,Nx):
        try:
            return (self.N+Nx.N)
        except AttributeError:
            return (self.N+Nx)
    def __mul__(self,Nx):
        try:
            return (self.N*Nx.N)
        except AttributeError:
            return (self.N*Nx)
    def __sub__(self,Nx):
        try:
            return (self.N-Nx.N)
        except AttributeError:
            return (self.N-Nx)
    def __mod__(self,Nx):
        try:
            return (self.N%Nx.N)
        except AttributeError:
            return (self.N%Nx)
    def __truediv__(self,Nx):
        try:
            return (self.N/Nx.N)
        except AttributeError:
            return (self.N/Nx)


class card:
    """card = 1 kartu"""

    def __init__(self,number,filename):
        self.N = number
        self.FN = filename

    def c2n():
        N=Numbers(self.N,str(self.N))
        return N
