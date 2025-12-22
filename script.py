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

for _,y in dataset_masini.iterrows():
    z = y["NPN"] + ";" + y["preposition"] + ";" + y["reduplicated_noun"] +  ";" + y["number_of_noun"] +  ";" + y["syntactic_function"] + ";" + y["meaning"]
    f = int(y["token_frequency"])
    lista_masini.append((z, f))
    
for _,y in dataset_a.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[8] + ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)

for _,y in dataset_su.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[8] + ";"+  y[10] +  ";" + y[9]
    lista_gorzoni.append(z)
    
for _,y in dataset_extra.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[8] + ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)
    
for _,y in dataset_add.iterrows():
    z = y[1] + ";" + y[3] + ";" + y[4] +  ";" + y[8] + ";" + y[10] +  ";" + y[9]
    lista_gorzoni.append(z)

gorzoni_list = list(Counter(lista_gorzoni).items())
# print(gorzoni_list)
# input()
# print(lista_masini)

m = 0
g = 0

# gorzoni_costr = []
# masini_costr = []

# while g < len(gorzoni_list):

#     col = gorzoni_list[g][0].split(";")
#     gorzoni_costr.append(col[0])
#     g+=1

# while m < len(lista_masini):

#     masini_costr.append(lista_masini[m][0])
#     m += 1



# g=0
# m=0

lista1 = sorted(lista_masini)
lista2 = sorted(gorzoni_list)

lista_completa = []

g=0
m=0

# casa.   cocomero.   cura
#                             ^
# casa.   cura.       drago
#.                      ^

while g<len(lista1) and m<len(lista2):
    
    el_lista1, f_l1 = lista1[g]
    el_lista2, f_l2 = lista2[m]
    
    if el_lista1 == el_lista2:
        lista_completa.append((el_lista1, f_l1, f_l2))
        m += 1
        g += 1
    elif el_lista1 < el_lista2:
        lista_completa.append((el_lista1, f_l1, 0))
        g += 1
    else:
        lista_completa.append((el_lista2, 0, f_l2))
        m += 1

while g<len(lista1) or m<len(lista2):
    while g<len(lista1):
        el_lista1, f_l1 = lista1[g]
        lista_completa.append((el_lista1, f_l1, 0))
        g += 1
    
    while m<len(lista2):
        el_lista2, f_l2 = lista2[m]
        lista_completa.append((el_lista2, 0, f_l2))
        m += 1

# while g<len(lista_gorzoni) and m<len(lista_masini):
    
#     col = gorzoni_list[g][0].split(";")
    

#     if col[0] in masini_costr:
#         for x in lista_masini:
#             if x[0] == col[0]:
#                 valore_masini = x[1]
#                 break

#         line = gorzoni_list[g][0] + ";" + str(valore_masini) + ";" + str(gorzoni_list[g][1])

#         nuovo_dataset.append(line)
        
#     if col[0] not in masini_costr: 
#         line = gorzoni_list[g][0] + ";0;" + str(gorzoni_list[g][1])

#         nuovo_dataset.append(line)
        
#     if lista_masini[m][0] not in gorzoni_costr:

#         line = str(lista_masini[m][0]) +";"+str(lista_masini[m][2])+";"+str(lista_masini[m][3])+";"+str(lista_masini[m][4])+";"+str(lista_masini[m][5])+ ";"+str(lista_masini[m][6])+ ";"+str(lista_masini[m][1]) + ";0"


#         nuovo_dataset.append(line)
    
#     m += 1
#     g+=1
    
    
print(len(lista_completa))


with open("dataset_finale.csv", "w", encoding="utf-8") as f:
    f.write("construction;preposition;lemma;pos;meaning;freq_masini;freq_gorzoni\n")
    
    for row in lista_completa:
        pre_row, f1, f2 = row
        f.write(f"{pre_row};{f1};{f2}\n")