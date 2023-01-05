import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, manhattan_distances
import seaborn as sns
import implicit
from sklearn.feature_extraction.text import TfidfVectorizer
import scipy.sparse as sparse
import matplotlib.pyplot as plt
from scipy.sparse.linalg import svds
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.preprocessing import MinMaxScaler

df_courses = pd.read_csv('(Responses).csv')
df_courses.drop(['Please choose 6  courses that you will choose /  interest you / have chosen  '], axis=1, inplace=True)

columns=['Gender', 'Business & Financial Technology (SIT)',
       'Information Technology (SIT)', 'Infocomm & Security (SIT)',
       'Cybersecurity  & Digital Forensics (SIT)',
       'Business Intelligence & Analytics (SIT)', 'Common ICT Programme (SIT)',
       'Experiential Product & Interior Design (SDM)',
       'Animation & Visual Effects (SDM)', 'Architecture  (SDM)',
       'Interaction Design (SDM)', 'Digital Game Art & Design (SDM)',
       'Visual Communication (SDM)', 'Motion Graphics Design (SDM)',
       'Game Development & Technology (SDM)', 'Applied Chemistry (SAS)',
       'Biologics & Process Technology (SAS)',
       'Chemical & Pharmaceutical Technology (SAS)',
       'Food Science & Nutrition (SAS)', 'Pharmaceutical Science (SAS)',
       'Accountancy & Finance (SBM)', 'Banking & Finance (SBM)',
       'Business Management (SBM)', 'Food & Beverage Business (SBM)',
       'Hospitality & Tourism Management (SBM)', 'Mass Media Management (SBM)',
       'Sport & Wellness Management (SBM)', 'Common Business Programme (SBM)',
       'Advanced & Digital Manufacturing (SEG)',
       'Aeronautical & Aerospace Technology (SEG)',
       'Aerospace Systems & Management (SEG)', 'AI & Data Engineering (SEG)',
       'Biomedical Engineering (SEG)',
       'Electronic & Computer Engineering (SEG)',
       'Engineering with Business (SEG)', 'Infocomm & Media Engineering (SEG)',
       'Nanotechnology & Materials Science (SEG)',
       'Robotics & Mechatronics (SEG)', 'Common Engineering Programme (SEG)',
       'Nursing (SHSS)', 'Oral Health Therapy (SHSS)', 'Social Work (SHSS)']
df_courses=df_courses[columns]


# grouping the gender so male 1 model , female  1 model

grp_dict = {}
test_data = {}
grp = df_courses.groupby(['Gender'])
for name, df in grp:
    df.drop(['Gender'], axis=1, inplace=True)
    df = df.reset_index().drop(['index'], axis=1)
    df_mat = np.array(df)
    test_indxs = []

    for i in range(len(df)): #extracting test data
        indxs = np.where(np.array(df.iloc[i]) == 1)[0]
        test_indx = np.random.choice(indxs, size=1)[0]
        df_mat[i][test_indx] = 0
        test_indxs.append(test_indx)
    test_data[name] = test_indxs
    grp_dict[name] = df_mat
keys = list(grp_dict.keys())
courses = np.array(df.columns)

df_anly = df_courses.groupby(['Gender']).sum().reset_index()
df_anly['group id'] = [i for i in range(len(df_anly))]


# using mahantaan distance and calc mahantaan simialriy , this one uses the distance first then minus off
def manhattan_similarity(matrix1, matrix2):
    manhattan_dist = manhattan_distances(matrix1, matrix2)
    scaler = MinMaxScaler()
    manhattan_dist_scaled = scaler.fit_transform(manhattan_dist)
    manhattan_sim = 1 - manhattan_dist_scaled
    return (manhattan_sim)


sim_mat_dic_m5 = {}
for i in range(len(keys)):
    df = grp_dict[keys[i]]
    data_matrix = np.array(df).T
    food_similarity_matrix = manhattan_similarity(data_matrix, data_matrix)
    sim_mat_dic_m5[keys[i]] = food_similarity_matrix


# recommend portion
def recommend(Gender, course, sim_mat, top_n):
    sim_mat = sim_mat[(Gender)]
    idx = np.where(courses == course)[0][0]
    sim_array = sim_mat[idx]
    sim_array[idx] = -1000
    scores = list(enumerate(sim_array))
    sorted_array = np.array(sorted(scores, key=lambda x: x[1], reverse=True), dtype='uint8')[:, 0]
    print(courses[sorted_array[:top_n]])
    return courses[sorted_array[:top_n]]


# test ######################
# Gender = 'Male'
# course = 'Common Business Programme (SBM)'
# recommend(Gender, course, sim_mat_dic_m5, 5)
#

