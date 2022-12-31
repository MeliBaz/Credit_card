
class Covjek:
    def __init__(self, ime,prezime,jmbg):
        self.__ime=ime
        self.__prezime=prezime
        self.__jmbg=jmbg
        
    def getIme(self):
        return self.__ime
    def setPrezime(self, prezime):
        if len(prezime)>1:
            return self.__prezime
        else:
            print("Unesite ponovno prezime!")
    def getPrezime(self):
        return self.__prezime        
        
        return self.__prezime
    def getJmbg(self):
        return self.__jmbg
 


class Klijent(Covjek):
    def __init__(self,ime,prezime,jmbg):
        super().__init__(ime, prezime, jmbg)
        self.__brojKartice=0
        
    def setBrojKartice(self,n):
        if Algoritam(n)==True:
            print("Broj kartice je validan")
        else:
            print("Broj kartice nije validan")
            
    def getBrojKartice(self):
        return self.__brojKartice
    
def Algoritam(n):
    a= n %10
    b=n//10
    lista=[]
    for i in range(0,len(str(b))):
        c=b%10
        d=b//10
        b=d
        lista.append(c)
    for i in range(0,len(lista),2):
        lista[i]=lista[i]*2
    suma=0
    lista2=[]
    suma=0
    for i in range(0, len(lista)):
        c=lista[i]%10
        d=lista[i]//10
        i=d
        suma=c+d
        lista2.append(suma)
    suma2=0
    for i in range(0,len(lista2)):
        suma2=suma2+lista2[i]
    Kartica=False
    if a==(10-(suma2%10))%10:
        Kartica=True
    return Kartica
        
    
        
print(Algoritam(12345674))

a1=Klijent("Neko", "Neko1", "12345567789 ")
print("Ime klijenta: ", a1.getIme())
print("Prezime klijenta: ", a1.getPrezime())
print("JMBG klijenta: ", a1.getJmbg())
a1.setBrojKartice(12345674)


   