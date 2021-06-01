import pandas as pd
from collections import Counter
import numpy as np

stroke = pd.read_csv('healthcare-dataset-stroke-data.csv')


stroke.drop('id', inplace=True, axis=1)
for c in stroke.columns:
    if c not in ['bmi', 'avg_glucose_level', 'age']:
        print(c, ":", Counter(stroke[c]))



nan = [np.nan]
print(stroke.query("bmi == @nan and smoking_status == 'Unknown'")) # no corellation


value_mapper_dict = {
    #Bartek: i think we should drop the other (one occurrence), or classify "other" as Female
    #Paweł: Yeah, that's only one data point, not worth examining imo
    'gender': {'Female': 0, 'Male': 1, 'Other': 2},
    'ever_married': {'No': 0, 'Yes': 1},
    # order is from frequency, values are my (Bartek) suggestions
    #Paweł: Sounds good
    'work_type': {'Private': 3, 'Self-employed': 4, 'children': 0, 'Govt_job': 2, 'Never_worked': 1},
    'Residence_type': {'Urban': 0, 'Rural': 1},
    # shouldn't 'unknown' be dropped or assigned to most frequent? (possible positive corelation between this one and 'children' in work type)
    #Paweł: Let's not drop unknown since it makes up much of a dataset. 
    'smoking_status': {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': 3},
}


for (k, v) in value_mapper_dict.items():
    stroke[k] = stroke[k].map(v)
print(stroke)


# should we map data from nominal to integer with count (most frequent are 0 and so on) (it could lead to inconsistence, (ex "Yes" is 0))
# or it should be decided by us like above

# what should we do with NaNs? (in bmi)

# should we classify age and bmi into ranges? (yes for bayes usage)
