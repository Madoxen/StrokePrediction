from numpy.core.fromnumeric import mean
import pandas as pd
from collections import Counter
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB
import numpy as np



stroke = pd.read_csv('healthcare-dataset-stroke-data.csv')


stroke = stroke.query("gender != 'Other'") # oh no 

stroke.drop('id', inplace=True, axis=1)
for c in stroke.columns:
    if c not in ['bmi', 'avg_glucose_level', 'age']:
        print(c, ":", Counter(stroke[c]))



nan = [np.nan]
print(stroke.query("bmi == @nan and smoking_status == 'Unknown'")) # no corellation



nominal_dict = {
    'age': {
        'bins': [0, 18, 35, 65],
        'names': ['0-18', '18-35', '35-65', '65+']
    },
    'avg_glucose_level': {
        'bins': [0, 70, 130],
        'names': ['low', 'normal', 'high']
    },
    'bmi': {
        'bins': [0, 18.5, 25, 30, 35],
        'names': ['underweight', 'normal', 'overweight', 'obese', 'extremely_obese']
    }

}

for i in nominal_dict.keys():
    pair = nominal_dict[i]
    d = dict(enumerate(pair['names'], 1))
    bins = pair['bins']

    stroke[i] = np.vectorize(d.get)(np.digitize(stroke[i], bins))

    


value_mapper_dict = {
    'gender': {'Female': 0, 'Male': 1},
    'ever_married': {'No': 0, 'Yes': 1},
    'work_type': {'Private': 3, 'Self-employed': 4, 'children': 0, 'Govt_job': 2, 'Never_worked': 1},
    'Residence_type': {'Urban': 0, 'Rural': 1},
    'smoking_status': {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': 3},
    'age': {'0-18': 0, '18-35': 1, '35-65': 2, '65+': 3},
    'avg_glucose_level': {'low': 0, 'normal': 1, 'high': 2},
    'bmi': {'underweight': 0, 'normal': 1, 'overweight': 2, 'obese': 3, 'extremely_obese': 4}
}

for (k, v) in value_mapper_dict.items():
    stroke[k] = stroke[k].map(v)
print(stroke)

stroke['bmi'] = stroke['bmi'].fillna(mean(stroke['bmi'].dropna())) #nans are assigned as mean

x = stroke.iloc[:,:-1]
y = stroke.iloc[:,-1]

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.20, random_state=1)

clf = GaussianNB()

clf.fit(x, y)

#test = [1,1,0,0,0,3,0,1,1,1] #Bartek

test = [1,2,1,0,1,4,0,1,1,0] #Bartek's dad

#test = [1,1,0,0,0,4,1,1,1,1] #Pawel

#test = [1,3,0,1,1,3,0,2,4,2] # testing for someone who got the stroke

X = np.array(test).reshape(1,-1)

print ("================================================================================= Prediction of : ", list(clf.predict(X)))
print(stroke.columns)