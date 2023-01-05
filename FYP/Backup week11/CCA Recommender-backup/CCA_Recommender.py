import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import seaborn as sns
import implicit
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.sparse as sparse
import matplotlib.pyplot as plt
from scipy.sparse.linalg import svds
sns.set(style = 'white')


df_cca=pd.read_csv('CCAPreferences.csv')
df_cca.drop(['UserID','Top 6 most preferred CCA','sum'], axis=1, inplace=True)

df_cca = df_cca.fillna(0)

grp_dict={}
test_data={}
grp = df_cca.groupby(['Gender','Age Group'])
# grouping the age and gender

for name, df in grp:
    df.drop(['Gender','Age Group'], axis=1, inplace=True)
    df=df.reset_index().drop(['index'],axis=1)
    df_mat=np.array(df)
    test_indxs=[]
    ### extract test data ###
    for i in range(len(df)):
        indxs=np.where(np.array(df.iloc[i])==1)[0]
        test_indx=np.random.choice(indxs, size=1)[0]
        df_mat[i][test_indx]=0
        test_indxs.append(test_indx)
    test_data[name]=test_indxs
    grp_dict[name]=df_mat
keys=list(grp_dict.keys())
ccas=np.array(df.columns)


df_anly=df_cca.groupby(['Gender','Age Group']).sum().reset_index()
df_anly['group id']=[i for i in range(len(df_anly))]

sim_mat_dic={}
for i in range(len(keys)):
    df=grp_dict[keys[i]]
    data_matrix=np.array(df).T
    cca_similarity_matrix=cosine_similarity(data_matrix,data_matrix) #Find the user-similarity matrix based on cosine similarity
    sim_mat_dic[keys[i]]=cca_similarity_matrix



def recommend(Gender,Age_Group,cca,sim_mat,top_n):
    sim_mat=sim_mat[(Gender,Age_Group)]#get which gender and agegroup then see which model to use
    idx=np.where(ccas==cca)[0][0]# get the cca and look through
    sim_array=sim_mat[idx]#put the index from the previous line into the sim_mat
    sim_array[idx]=-1000 # minus 1000 to get the idx, forcing that value to large negetive value.
    scores=list(enumerate(sim_array))#To specify each course of a sequence individually
    sorted_array=np.array(sorted(scores,key=lambda x: x[1], reverse=True),dtype='uint8')[:,0]# sort and print top 5
    print(ccas[sorted_array[:top_n]])
    return ccas[sorted_array[:top_n]]