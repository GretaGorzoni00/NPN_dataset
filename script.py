import pandas as pd
from collections import Counter	

lista_masini =[]
lista_gorzoni =[]
gorzoni_list =[]
nuovo_dataset =[]

df_filtrato = pd.read_csv("dataset_Masini.csv", sep=";")

dataset_masini = df_filtrato[df_filtrato["preposition"].isin(["a", "su"])]
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

 
 
m = 0
g = 0



gorzoni_costr = []
masini_costr = []

while g < len(gorzoni_list):

    col = gorzoni_list[g][0].split(";")
    gorzoni_costr.append(col[0])
    g+=1
    
while m < len(lista_masini):

    masini_costr.append(lista_masini[m][0])
    m += 1



g=0
m=0

while g < len(gorzoni_list) and m < len(lista_masini):
    
    col = gorzoni_list[g][0].split(";")
    

    if col[0] in masini_costr:
        for x in lista_masini:
            if x[0] == col[0]:
                valore_masini = x[1]
                break

        line = gorzoni_list[g][0] + ";" + str(valore_masini) + ";" + str(gorzoni_list[g][1])

        nuovo_dataset.append(line)
        
    if col[0] not in masini_costr: 
        line = gorzoni_list[g][0] + ";0;" + str(gorzoni_list[g][1])

        nuovo_dataset.append(line)
        
    if lista_masini[m][0] not in gorzoni_costr:

        line = str(lista_masini[m][0]) +";"+str(lista_masini[m][2])+";"+str(lista_masini[m][3])+";"+str(lista_masini[m][4])+";"+str(lista_masini[m][5])+ ";"+str(lista_masini[m][6])+ ";"+str(lista_masini[m][1]) + ";0"


        nuovo_dataset.append(line)
    
    m += 1
    g+=1
    
    
print(len(nuovo_dataset))


with open("dataset_finale.csv", "w", encoding="utf-8") as f:
    # header (adatta i nomi se vuoi)
    f.write("construction;preposition;lemma;pos;meaning;freq_masini;freq_gorzoni\n")
    
    for row in nuovo_dataset:
        f.write(row + "\n")