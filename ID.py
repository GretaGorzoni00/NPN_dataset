import pandas as pd

# CORIS_annotato_add = pd.read_csv("distractor.csv", sep=";")

# start_id = 4247
# CORIS_annotato_add['ID'] = range(start_id, start_id + len(CORIS_annotato_add))

# CORIS_annotato_add.to_csv("distractor.csv", sep= ";", index=False)

d1= pd.read_csv("data/A_distractor.csv", sep=";")
d2= pd.read_csv("data/SU_distractor.csv", sep=";")
d3= pd.read_csv("distractor.csv", sep=";")


tutto_dataset = pd.concat([d1, d2, d3])

tutto_dataset.to_csv("distractor.csv", sep=";", index=False)

df = pd.read_csv("distractor.csv", sep = ";")

df = df.drop("construction",  axis=1)

df.to_csv("distractor.csv", sep=";", index=False)


