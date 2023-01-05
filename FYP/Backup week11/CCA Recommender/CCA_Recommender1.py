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

df_ccas = pd.read_csv('CCAPreferences.csv')
df_ccas.drop(['Top 6 most preferred CCA'], axis=1, inplace=True)

columns=['Gender', 'Adventure Club (Sports and Adventure)',
         'Aikido (Sports and Adventure)', 'Ambassadorial Team (Leadership & Character Development)',
         'Archery (Sports and Adventure)', 'Astronomy Club (Leadership & Character Development)',
         'Athletics (Sports and Adventure)', 'Badminton (Sports and Adventure)',
         'Basketball (Sports and Adventure)', 'Bei Quan Dao (Sports and Adventure)',
         'Bowling (Sports and Adventure)', 'Buddhist Society (Societies)',
         'Canoe Sprint (Sports and Adventure)', 'Catholic Youth Community (Societies)',
         'CD Lionhearters (Community Service & Environment)', 'Chinese Cultural Group (Arts & Culture)',
         'Chinese Orchestra (Arts & Culture)', 'Community Service Club (Community Service & Environment)',
         'Crew Studio (Arts & Culture)', 'Current Affairs & Debating Club (Leadership & Character Development)',
         'Dance Company (Arts & Culture)', 'Danz Inc. (Arts & Culture)',
         'Der Treff German Club (Arts & Culture)', 'Dragonboat (Sports and Adventure)',
         'Emcee Club (Community Service & Environment)', 'Entrepreneurship Club (Leadership & Character Development)',
         'Floorball (Sports and Adventure)', 'Foreign Bodies (Arts & Culture)',
         'Geo Council (Community Service & Environment)', 'Guitar Club (Arts & Culture)',
         'Harmonica Ensemble (Arts & Culture)', 'Hockey (Sports and Adventure)',
         'Indian Cultural Group (Arts & Culture)', 'Judo (Sports and Adventure)',
         'Kendo (Sports and Adventure)', 'K-Wave Korean Club (Arts & Culture)',
         'L Hexagone French Club (Arts & Culture)', 'La Ballroom En Masse (Arts & Culture)',
         'Leo Club (Community Service & Environment)', 'Library Champions (Leadership & Character Development)',
         'Life Saving (Sports and Adventure)', 'Lion & Dragon Dance Troupe (Sports and Adventure)',
         'Live Audio (Arts & Culture)', 'Makers Innovators Tribe (Leadership & Character Development)',
         'Makeup Artistry (Arts & Culture)', 'Malay Cultural Group (Arts & Culture)',
         'Mentoring Club (Community Service & Environment)', 'Mindsports (Sports and Adventure)',
         'Netball (Sports and Adventure)', 'Nyaa Students Club (Community Service & Environment)',
         'NYP Cru (Societies)', 'NYP Primers (Community Service & Environment)',
         'Peer Supporter Club (Community Service & Environment)', 'Photography Club (Leadership & Character Development)',
         'Piano Ensemble (Arts & Culture)', 'Running Club (Sports and Adventure)',
         'Sakuran Japanese Cultural Club (Arts & Culture)', 'SAS Club (Academic Club)',
         'SBM Club (Academic Club)', 'SDM Club (Academic Club)', 'SEG Club (Academic Club)',
         'Service Learning Group (Community Service & Environment)', 'SHSS Club (Academic Club)',
         'Silat (Sports and Adventure)', 'SIT Club (Academic Club)', 'Sketch Art Club (Arts & Culture)',
         'Soccer (Sports and Adventure)', 'Soundcard (Arts & Culture)', 'Squash (Sports and Adventure)',
         'Stagearts Drama & Theatre Management Club (Arts & Culture)', 'Street Workout Club (Sports and Adventure)',
         'Strongman Club (Sports and Adventure)', 'Students Union (Leadership & Character Development)',
         'Swimming (Sports and Adventure)', 'Symphony Orchestra (Arts & Culture)',
         'Table Tennis (Sports and Adventure)', 'Taekwondo (Sports and Adventure)',
         'Tchoukball (Sports and Adventure)', 'Tennis (Sports and Adventure)',
         'The Communicators (Leadership & Character Development)', 'Touch Football (Sports and Adventure)',
         'Ultimate Frisbee (Sports and Adventure)', 'Voice Ensemble (Arts & Culture)',
         'Volleyball (Sports and Adventure)', 'Zhong Hua Wushu (Sports and Adventure)']
df_ccas=df_ccas[columns]


# grouping the gender so male 1 model , female  1 model

grp_dict = {}
test_data = {}
grp = df_ccas.groupby(['Gender'])
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
ccas = np.array(df.columns)

df_anly = df_ccas.groupby(['Gender']).sum().reset_index()
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
def recommend(Gender, cca, sim_mat, top_n):
    sim_mat = sim_mat[(Gender)]
    idx = np.where(ccas == cca)[0][0]
    sim_array = sim_mat[idx]
    sim_array[idx] = -1000
    scores = list(enumerate(sim_array))
    sorted_array = np.array(sorted(scores, key=lambda x: x[1], reverse=True), dtype='uint8')[:, 0]
    print(ccas[sorted_array[:top_n]])
    return ccas[sorted_array[:top_n]]
