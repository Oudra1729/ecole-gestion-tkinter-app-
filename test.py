from Classes import *
from Functions import *
from datetime import *
from uuid import uuid4
from prettytable import PrettyTable
# S=Stagaire(123,"kamel","ismael",date(1998,8,23),"DD")
# # print(S)


dn=date(1998,8,23)
da=date(2016,8,23)

# print(int((da-dn).days/365.25))
file="Directure.csv"
User="admin"
Pass = "ista"

# if confirmeUtl(User,Pass,file):
#     print("Acces autorisé")
# else :
#     print("Acces non autorisé")

# MenuDrctr()
#- MenuFrmtr()

M1=Module("PHP",1,2,"PA122")
M2=Module("CSS",1,1,"PA457")
M3=Module("Python",1,2,"PA789")
M4=Module("HTML",1,1,"PA123")
LM=[M1,M2,M3,M4]
# print(Inscription())
DD=Filiere("Developpement Digital","DD",LM)
GE=Filiere("Gestion Des Entreprises","GE",LM)

F1=Formateur('P12345','Ait elka','Ismael',date(1998,8,23),LM)
F2=Formateur('P1234s5','Ait elka','Ismael',date(1998,8,23),LM)
LFO=[F1,F2]
# print(DD)
# print(GE)
ListFiliere=[DD,GE]
S1=Stagaire("PA2215",1,"Ait El Kamel","Ismael",date(1998,8,23),ListFiliere,11.66)
S2=Stagaire("PA2245",1,"Oudra","Brahim",date(1999,6,15),ListFiliere,11.58)
S3=Stagaire("PA2875",2,"Aassab","Hiba",date(2002,6,26),ListFiliere,14.74)
S4=Stagaire("PA2645",1,"Er-Rachedy","Yassine",date(2000,10,16),ListFiliere,14.98)
S5=Stagaire("PA2240",1,"Ait Lhassan","Ayoub",date(2004,8,20),ListFiliere,14.42)
# print(S)
# print(S2)
# LN=["SQL","JS","RUBY","JAVA"]
# print(LM + LN)
LA=[S1,S2,S3,S4,S5]
LS=[]
# afficherModules(LM)
# AfficherStagaire(LA)
# AfficherFormateurs(LFO)
# SupremeFrmtr(LFO)
# for stg in LFO:
#     print(stg)
N1=Note(1,"PA2215",12.5,17.75,15.00)
N2=Note(2,"PA2215",19.5,19.75,18.00)
N3=Note(3,"PA2215",17.5,19.25,18.00)
N4=Note(4,"PA2215",18.5,18.75,19.00)

LN=[N1,N2,N3,N4]


# fonction pour ressudre l'erreur de integer 

O= [0,1,2,3,4,5]

def EntDate(min,max,msg):
    while True:
        try:
            N = int(input(msg))
            if N >= min and N <= max:
                return N
            else:
                print("La valuer donnée non valide ")
        except (ValueError):
            print("Entrée invalide !!")

j=EntDate(1,31,"entrez le jour :")
m=EntDate(1,12,"entrez le mois :")
a=EntDate(1900,2015,"entrez l'anné :")

print(j,m,a)

