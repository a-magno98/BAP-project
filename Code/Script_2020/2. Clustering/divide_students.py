import pandas as pd

#output weka 
file = "data_in_clusters.csv"

#file cleaned
file_data = "tableau_data2020.csv"

#load output weka
df = pd.read_csv(file, encoding='utf-8')

#load cleaned data
df_data = pd.read_csv(file_data, encoding='utf-8', sep=';')

#filter students in cluster1/2/3/4
stu_cl1 = df.User[df.Cluster == 'cluster1']
stu_cl2 = df.User[df.Cluster == 'cluster2']
stu_cl3 = df.User[df.Cluster == 'cluster3']
stu_cl4 = df.User[df.Cluster == 'cluster4']

stu_cl1 = stu_cl1.reset_index(drop=True)
list_stu_cl1 = stu_cl1.to_list()

stu_cl2 = stu_cl2.reset_index(drop=True)
list_stu_cl2 = stu_cl2.to_list()

stu_cl3 = stu_cl3.reset_index(drop=True)
list_stu_cl3 = stu_cl3.to_list()

stu_cl4 = stu_cl4.reset_index(drop=True)
list_stu_cl4 = stu_cl4.to_list()


data_student_cl1 = df_data[df_data.User.isin(list_stu_cl1)]
data_student_cl2 = df_data[df_data.User.isin(list_stu_cl2)]
data_student_cl3 = df_data[df_data.User.isin(list_stu_cl3)]
data_student_cl4 = df_data[df_data.User.isin(list_stu_cl4)]

data_student_cl1.to_csv("cluster1.csv", index=False)
data_student_cl2.to_csv("cluster2.csv", index=False)
data_student_cl3.to_csv("cluster3.csv", index=False)
data_student_cl4.to_csv("cluster4.csv", index=False)




