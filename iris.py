from joblib import dump, load
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

RANDOM_SEED = 17 # because it's the most popular random number between 1 and 20

data=load_iris()


#Create a pipeline 

pipeline = Pipeline([
    ('features', FeatureUnion([
        ('poly', PolynomialFeatures()),
        ('scaler', StandardScaler())
    ])),
    ('logreg', LogisticRegression(random_state=RANDOM_SEED))
])

#using the whole dataset - 150 observations

features = data.data

target = np.array([data.target_names[x] for x in data.target]).reshape(-1, 1)

pipeline.fit(features,target)


# dump the model using joblib
#---------------------------------------
dump(pipeline, 'iris.joblib')
#---------------------------------------

# this can be loaded again into our web app by the following command.

model=load('iris.joblib')

