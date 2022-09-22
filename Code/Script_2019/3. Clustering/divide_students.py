import pandas as pd

#output weka 
file = "data_in_clusters.csv"

#file cleaned
file_data = "cleaned_data.csv"

#load output weka
df = pd.read_csv(file, encoding='utf-8')

#load cleaned data
df_data = pd.read_csv(file_data, encoding='utf-8')

#filter students in cluster0 and cluster1
stu_cl0 = df.User[df.Cluster == 'cluster0']
stu_cl1 = df.User[df.Cluster == 'cluster1']

stu_cl0 = stu_cl0.reset_index(drop=True)
list_stu_cl0 = stu_cl0.to_list()

stu_cl1 = stu_cl1.reset_index(drop=True)
list_stu_cl1 = stu_cl1.to_list()


data_student_cl0 = df_data[df_data.User.isin(list_stu_cl0)]
data_student_cl1 = df_data[df_data.User.isin(list_stu_cl1)]

data_student_cl0.to_csv("cluster0.csv", index=False)
data_student_cl1.to_csv("cluster1.csv", index=False)




