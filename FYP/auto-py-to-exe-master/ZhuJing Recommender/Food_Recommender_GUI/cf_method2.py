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


df_food=pd.read_csv('newfooddata2 - Sheet1.csv')
df_food.drop(['UserID','Top 6 most preferred dishes','sum'], axis=1, inplace=True)


grp_dict={}
test_data={}
grp = df_food.groupby(['Gender','Age Group'])
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
foods=np.array(df.columns)


df_anly=df_food.groupby(['Gender','Age Group']).sum().reset_index()
df_anly['group id']=[i for i in range(len(df_anly))]

sim_mat_dic_svd={}
for i in range(len(keys)):
    df=grp_dict[keys[i]]
    R = np.array(df).T
    mean = np.mean(R, axis = 1)
    data_matrix = R - mean.reshape(-1, 1)
    U, sigma, Vt = svds(data_matrix, k = np.min(data_matrix.shape)-1)
    sigma = np.diag(sigma)
    feature_matrix=np.dot(U, sigma)
    food_similarity_matrix=cosine_similarity(feature_matrix,feature_matrix) #Find the user-similarity matrix based on cosine similarity
    sim_mat_dic_svd[keys[i]]=food_similarity_matrix


def recommend(Gender,Age_Group,food,sim_mat,top_n):
    sim_mat=sim_mat[(Gender,Age_Group)]
    idx=np.where(foods==food)[0][0]
    sim_array=sim_mat[idx]
    sim_array[idx]=-1000
    scores=list(enumerate(sim_array))
    sorted_array=np.array(sorted(scores,key=lambda x: x[1], reverse=True),dtype='uint8')[:,0]
    print(foods[sorted_array[:top_n]])
    return foods[sorted_array[:top_n]]


#test
Gender='Female'
Age_Group='14 and below'
food='Fish and Chips'

recommend(Gender,Age_Group,food,sim_mat_dic_svd,5)

#results
# ['Fish and Chips' 'Roti Prata' 'hainanese chicken rice' 'Hokkien Mee'
#  'Cereal Prawn']
