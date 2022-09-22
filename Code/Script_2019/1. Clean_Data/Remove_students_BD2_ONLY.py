import pandas as pd

#file from tableau prep
file = 'tableau_data2019.csv'

#file received original
file_original = 'AnonimyzedLogBD+BD2_2019.csv'

#load tableau file output
df_cleaned = pd.read_csv(file, encoding='utf-8', sep=';')

#load file original
df_original = pd.read_csv(file_original, encoding='utf-8')

#Find students who are bd2 only 
columns = ['utente', 'evento']
subset = pd.DataFrame(df_original, columns = columns)


data = subset.loc[subset['evento'].str.contains('Corso')==True]
data = data[~data.utente.str.contains('/')]

clean_dupl = data.drop_duplicates()

df_drop = clean_dupl.drop_duplicates(subset='utente')
bd2_only = df_drop.loc[df_drop['evento'].str.contains('27054')==True]

bd2_only = bd2_only.loc[:, 'utente']
bd2_only_numb = bd2_only.str.extract('(\d+)', expand=False)

df_cleaned = df_cleaned[~df_cleaned['User'].isin(bd2_only_numb.to_list())]

#esport data in csv
df_cleaned.to_csv("cleaned_data.csv", index=False)

###########################################################################

##Calculate nbr students who study bd and bd2
bd_2 = data.loc[data['evento'].str.contains('27054')==True]
bd_2 = bd_2.drop_duplicates(subset='utente')
bd_2 = bd_2[~bd_2['utente'].isin(bd2_only.to_list())]

##Calculate nbr students who study bd only
bd_only = data.loc[data['evento'].str.contains('25880')==True]
bd_only = bd_only.drop_duplicates(subset='utente')
bd_incl = bd_only
bd_only = bd_only[~bd_only['utente'].isin(bd_2.utente.to_list())]

print("Number of students BD2 only: ", bd2_only.shape[0])
print("Number of students BD+BD2: ", bd_2.shape[0])
print("Number of students BD only: ", bd_only.shape[0])
print("Number total BD (include BD2): ", bd_incl.shape[0])


