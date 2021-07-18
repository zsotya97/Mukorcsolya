#Osztály a rövidprogramhoz
class RovidProgram(object):
    def __init__(self, sor):
        split=sor.split(";")
        self.Nev = split[0]
        self.Orszag = split[1]
        self.Technikai= float(split[2])
        self.Komponens= float(split[3])
        self.Hibapont= float(split[4])

    def Osszpontszam(self):
        return self.Technikai+self.Komponens-self.Hibapont
#Osztály a végeredmény felállításához
class Vegeredmeny:
    def __init__(self, nev, orszag,pont):
        self.Nev = nev
        self.Orszag = orszag 
        self.Pont=pont

#Osztály a dÖntő dokumentumhoz
class Donto(RovidProgram):
    def __init__(self,sor):
        super().__init__(sor)
#Beolvasás függvény
def Beolvasas(dokumentum, osztaly):
    with open(dokumentum, "r", encoding="utf-8")as Beolvas:
        fejlec= Beolvas.readline()
        return [osztaly(x.strip()) for x in Beolvas]
#Metódus a 4. feladathoz
def Eredmeny(nev,rovid, donto):
    eredmeny=0
    for x in rovid:
        if x.Nev == nev:
            volt = False
            for y in donto:
                if y.Nev == nev: 
                    volt = True
                    eredmeny+= y.Osszpontszam()+x.Osszpontszam()
                    break
            if volt == False:  eredmeny+= x.Osszpontszam()
    return eredmeny
        


#Adatok beolvasása
rovid = Beolvasas("rovidprogram.csv",RovidProgram)
donto = Beolvasas("donto.csv",Donto)

#2. feladat
print(f"2.feladat:\n\tA rövidprogramban {len(rovid)} induló volt")

#3. feladat
magyar = False
for x in donto:
    if x.Orszag.lower()=="hun": 
        magyar=True
        break
print("3. feladat:", end="\n\t")
voltmagyar = "A magyar versenyző bejutott a kűrbe" if magyar==True else "A magyar versenyző nem jutott be a kűrbe"
print(voltmagyar)

#5. feladat
versenyzo = input("5. feladat: \n\tKérem a versenyző nevét: ")
volt = False

#6. feladat
print("6. feladat: ")
for x in rovid:
    if versenyzo == x.Nev: 
        print(f"\tA versenyző összpontszáma: {Eredmeny(versenyzo, rovid, donto)}")
        volt=True
        break
print("\tNem volt ilyen versenyző") if volt == False else None

#7. feladat
print("7. feladat: ")
statisztika = {x.Orszag for x in donto}
for x in statisztika:
    szamolas=0
    for y in donto:
        if x == y.Orszag: szamolas+=1
    if szamolas > 1:
        print(f"\t{x}: {szamolas} versenyző")


#8. feladat
szamlalas=0
with open("vegeredmeny.csv","w",encoding="utf8") as Kiir:
    stat_lista =[Vegeredmeny(x.Nev, x.Orszag, Eredmeny(x.Nev,rovid, donto)) for x in rovid]
    for x in sorted(stat_lista, key=lambda x: x.Pont, reverse=True):
        szamlalas+=1
        Kiir.write(f"{szamlalas};{x.Nev};{x.Orszag};{x.Pont:.2f}\n")
print("8. feladat: vegeredmeny.csv")