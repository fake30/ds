import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("wholesale.csv")

# Separate features
categorical_features = ['Channel', 'Region']
continuous_features = ['Fresh', 'Milk', 'Grocery', 'Frozen', 'Detergents_Paper', 'Delicassen']

# Convert categorical variables to dummy/one-hot encoding
for col in categorical_features:
    dummies = pd.get_dummies(data[col], prefix=col)
    data = pd.concat([data, dummies], axis=1)
    data.drop(col, axis=1, inplace=True)

# Normalize the data
mms = MinMaxScaler()
data_transformed = mms.fit_transform(data)

# K-means clustering for a range of k values
sum_of_squared_distances = []
K = range(1, 15)

for k in K:
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(data_transformed)
    sum_of_squared_distances.append(km.inertia_)

# Elbow plot
plt.plot(K, sum_of_squared_distances, 'bx-')
plt.xlabel('k')
plt.ylabel('Sum of Squared Distances') 
plt.title('Elbow Method for Optimal k') 
plt.show()
