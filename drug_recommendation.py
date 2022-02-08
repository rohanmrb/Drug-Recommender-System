import pandas as pd
import numpy as np
import math
from sklearn.metrics.pairwise import cosine_similarity as cs
df=pd.read_csv('Drug data.csv')
df=df[['drug','contents','diseases']]
disease=[]
d=[]

#reccomendation based on disease
print('''
     reccomendation based on disease

     ''' )
for i in df['diseases']:
 i=str(i)
 m=list(i.split(sep=","))
 d.append(list(m))
 for j in m:
  disease.append(j)
disease=list(set(disease))
# print(disease)
disease=["allergy"]

matrix=[]
for i in range(len(df['diseases'])):
    matrix.append(list())


for i in range(len(d)):
    for j in range(len(disease)):
        if disease[j] in d[i]:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

cosine_sim=cs(matrix)
# print(cosine_sim)

arr = []
for i in cosine_sim:
    arr.append(sum(i))

scores_series=pd.Series(arr).sort_values(ascending=False)
# print(scores_series)
recommended_indexes=list(scores_series[0:5].index)
recommend=[]
for i in recommended_indexes:
    recommend.append(df["drug"][i])
print(recommend)


#reccomendation based on contents
print('''
     reccomendation based on contents of the drug

     ''' )
contents=[]
c=[]

for i in df['contents']:
    i=str(i)
    m=list(i.split(sep=','))
    c.append(list(m))
    for j in m:
        contents.append(j)
contents=list(set(contents))
# print(contents)
contents=["Paracetamol","Cetirizine"]

matrix=[]
for i in range(len(df['contents'])):
    matrix.append(list())

for i in range(len(c)):
    for j in range(len(contents)):
        if contents[j] in c[i]:
            matrix[i].append(1)
        else:
            matrix[i].append(0)

cosine_sim=cs(matrix)

# print(cosine_sim)
arr = []
for i in cosine_sim:
    arr.append(sum(i))

scores_series=pd.Series(arr).sort_values(ascending=False)
recommended_indexes=list(scores_series[0:5].index)
recommend=[]
for i in recommended_indexes:
    recommend.append(df["drug"][i])
print(recommend)
