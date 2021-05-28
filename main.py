import pandas as pd
from collections import Counter


stroke = pd.read_csv('healthcare-dataset-stroke-data.csv')


stroke.drop('id', inplace=True, axis=1)
for c in stroke.columns:
    if c not in ['bmi', 'avg_glucose_level', 'age']:
        print(c, ":", Counter(stroke[c]))


value_mapper_dict = {
    # i think we should drop the other (one occurrence), or classify "other" as Female
    'gender': {'Female': 0, 'Male': 1, 'Other': 2},
    'ever_married': {'No': 0, 'Yes': 1},
    # order is from frequency, values are my (Bartek) suggestions
    'work_type': {'Private': 3, 'Self-employed': 4, 'children': 0, 'Govt_job': 2, 'Never_worked': 1},
    'Residence_type': {'Urban': 0, 'Rural': 1},
    # shouldn't 'unknown' be dropped or assigned to most frequent? (possible positive corelation between this one and 'children' in work type)
    'smoking_status': {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': 3},
}


for (k, v) in value_mapper_dict.items():
    stroke[k] = stroke[k].map(v)

print(stroke)

# should we map data from nominal to integer with count (most frequent are 0 and so on) (it could lead to inconsistence, (ex "Yes" is 0))
# or it should be decided by us like above

# what should we do with NaNs? (in bmi)

# should we classify age and bmi into ranges? (yes for bayes usage)
