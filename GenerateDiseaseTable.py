import pandas as pd 
diseases = ['J411', 'I269', 'J180', 'I693', 'I109', 'J340']
names = ['mucocorpulent chronic bronchitis', 'pulmonary embolism without mention of acute cor pulmonale', 'bronchopneumonia unspecifiied', 'sequelae of cerebral infraction', 'other and unspecified primary hypertension', 'abscess, furuncle, and carbuncle of nose']

df = pd.DataFrame(names, index=diseases, columns=['disease_name'])
print(df)

df.to_csv('data/disease_code_conversion.csv')