lista1 =["CLANG", "COCOONING", "COHOUSING", "COSTING", "COUNSELING", "COUNSELLING", "CRACKING", "CROWDSOURCING", "CURLING", "CUTTING", "CYBORG", "DAMPING", "DANCING", "DATING", "DEBUG", "DEBUGGING", "DECOMMISSIONING", "DELISTING", "DIVING", "DOCKING", "DONG", "DOPING", "DOWNGRADING", "DRAFTING", "DRIBBLING", "DRIPPING", "DUMPING", "ERG", "ERLANG", "EXTRASTRONG", "FADING"]

lista2 = ["CLANG", "CLEARING", "COSTING", "COUNSELING", "COUNSELLING", "CRACKING", "CROWDSOURCING", "CURLING", "CUTTING", "CYBORG", "DAMPING", "DANCING", "DATING", "DEBUG", "DEBUGGING", "DECOMMISSIONING", "DELISTING", "DIVING", "DOCKING", "DONG", "DOPING", "DOWNGRADING", "DRAFTING", "DRIBBLING", "DRIPPING", "DUMPING", "EDITING", "ELETTROSMOG", "ENGINEERING", "FACTORING", "FADING"]

lista1 = sorted(lista1)
lista2 = sorted(lista2)

lista_completa = []

g=0
m=0

while g<len(lista1) and m<len(lista2):
    
    el_lista1 = lista1[g]
    el_lista2 = lista2[m]
    
    if el_lista1 == el_lista2:
        lista_completa.append(el_lista1)
        m += 1
        g += 1
    elif el_lista1 < el_lista2:
        lista_completa.append(el_lista1)
        m += 1
    else:
        lista_completa.append(el_lista2)
        g += 1


while g<len(lista1) or m<len(lista2):
    while g<len(lista1):
        el_lista1 = lista1[g]
        lista_completa.append(el_lista1)
        g += 1
    
    while m<len(lista2):
        el_lista2 = lista2[m]
        lista_completa.append(el_lista2)
        m += 1