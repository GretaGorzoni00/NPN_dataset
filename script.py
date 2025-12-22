import pandas as pd
from collections import Counter	

lista_masini =[]
lista_gorzoni =[]
gorzoni_list =[]
nuovo_dataset =[]

dataset_masini = pd.read_csv("dataset_Masini.csv", sep=";")
dataset_extra = pd.read_csv("CORIS_annotato_extra.csv", sep=";")
dataset_add = pd.read_csv("CORIS_annotato_add.csv", sep=";")
dataset_a = pd.read_csv("data/A_construction.csv", sep=";")
dataset_su = pd.read_csv("data/SU_construction.csv", sep=";")

for _,x in dataset_masini.iterrows():
    lista_masini.append(x)

for _,y in dataset_a.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)
 
for _,y in dataset_su.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)
    
for _,y in dataset_extra.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)
    
for _,y in dataset_add.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)
 
gorzoni = Counter(lista_gorzoni)
for key, value in gorzoni.items():
    o = key, value
    gorzoni_list.append(o)

print(len(gorzoni_list)) 
print(gorzoni_list[78][1])    
 
m = 0
g = 0


print(len(lista_masini))

while g < len(gorzoni_list):


    for el in lista_masini:
   
        if gorzoni_list[g][0] == lista_masini[el][0]:
            nuovo_dataset.append()
            
        if gorzoni_list[g][0] != lista_masini[el][0]:    
            nuovo_dataset.append(gorzoni_list[g])
    g += 1
    
    
    
print(len(lista_masini))   