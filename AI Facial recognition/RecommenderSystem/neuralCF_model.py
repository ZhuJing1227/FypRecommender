import pandas as pd
import numpy as np
from zipfile import ZipFile
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path
import matplotlib.pyplot as plt

df = pd.read_csv('newfooddata2 - Sheet1.csv')


df.Gender = pd.Categorical(df.Gender)
df['gender_index'] = df.Gender.cat.codes

df['Age Group'] = pd.Categorical(df['Age Group'])
df['age_group_index'] = df['Age Group'].cat.codes


cols = df.columns.tolist()
new_cols = cols[29:] + cols[4:28]
df_as_list = df.values.tolist()


prep_data_list = []
for i in range(len(df_as_list)):
  curr_gender = df_as_list[i][0]
  curr_age_gp = df_as_list[i][1]
  for j in range(2, 26):
    if df_as_list[i][j] == 1: #  user indicated their preference for this food
      for k in range(2, 26):
        if df_as_list[i][k] == 1 and k != j: #  user indicated their preference for this food and not same food
          # gender, age group, indicated food, recommended food
          prep_data_list.append([curr_gender, curr_age_gp, j-2, k-2]) # -  2 to make food zero idx

prepped_df = pd.DataFrame(prep_data_list, columns=['gender', 'age_group', 'indicated_food', 'rcmd_food'])

from sklearn.preprocessing import OneHotEncoder

# do one hot encoding
one_hot_encoder = OneHotEncoder(sparse=False)
one_hot_encoder.fit(prepped_df[['gender', 'age_group', 'indicated_food']])

prepped_df_encoded = one_hot_encoder.transform(prepped_df[['gender', 'age_group', 'indicated_food']])
prepped_df_encoded = pd.DataFrame(data=prepped_df_encoded)
prepped_df_encoded['rcmd_food'] = prepped_df['rcmd_food']
train_df = prepped_df_encoded.head(int(prepped_df.shape[0] * 0.8))
val_df = prepped_df_encoded.tail(int(prepped_df.shape[0] * 0.2))


#create  neural and train
train_x = train_df.iloc[:,:-1]
train_y = train_df['rcmd_food']

val_x = val_df.iloc[:,:-1]
val_y = val_df['rcmd_food']


model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'), # hidden layer
    tf.keras.layers.Dense(24) # number of food type
])


model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_x, train_y, epochs=80)

test_loss, test_acc = model.evaluate(val_x,  val_y, verbose=2)

print('\nTest accuracy:', test_acc)

# setup prediction model
probability_model = tf.keras.Sequential([model,
                                         tf.keras.layers.Softmax()])

gender_vec = np.zeros(2)
gender_vec[1] = 1
age_gp_vec = np.zeros(5)
age_gp_vec[3] = 1
food_vec = np.zeros(24)
food_vec[10] = 1

#  concatenate them into one input vector for the neural network model
user_input_vec = tf.concat([gender_vec, age_gp_vec, food_vec], axis=0)
user_input_vec = tf.expand_dims(user_input_vec, axis=0)

#predictions
predictions = probability_model.predict(user_input_vec)
# get numpy argsort
rcmd_food_indices = np.argsort(predictions)[0][-5:]


#recommendations
print(rcmd_food_indices)
