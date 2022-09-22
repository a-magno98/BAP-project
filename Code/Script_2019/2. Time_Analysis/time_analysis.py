import pandas as pd
from datetime import *

#file cleaned with BD students
file = 'cleaned_data.csv'

df = pd.read_csv(file, encoding='utf-8')

#convert string Time to DateTime
df['Time'] = pd.to_datetime(df['Time'], format='%d/%m/%Y %H:%M')

df = df.sort_values(by=['User','Time'])

df['Day'] = df.Time.dt.day
df['Month'] = df.Time.dt.month
df['Year'] = df.Time.dt.year

#for debug
pd.set_option('display.max_rows', df.shape[0]+1)

#calculate the difference between two actions in sequence
df['Diff_Time'] = df.Time.shift(-1) - df.Time

#find index to set Diff_Time to 0
ind = df.index[(df.Day != df.Day.shift(-1)) | (df.Month != df.Month.shift(-1)) | (df.Year != df.Year.shift(-1)) | (df.User != df.User.shift(-1))]
df['Diff_Time'].loc[ind.to_list()] = timedelta(0,0)

##copy
df2 = df.copy()
df3 = df.copy()
df4 = df.copy()

#filter selecting the resource which means time spent in theory
df = df[df.Information == 'Resource']
df_groupby = df.groupby(['User', 'Information', 'Month'])['Diff_Time'].sum()
df_groupby.columns = ['User', 'Information', 'Month', 'Diff_Time']
df_groupby = df_groupby.reset_index()
df_groupby = df_groupby.rename(columns={'Diff_Time':'Time_Theory'})

#calculate the time spent on theory in hours
df_groupby['Time_Theory']=[(int)(df_groupby.Time_Theory[i].total_seconds()//3600) for i in range(len(df_groupby['Time_Theory']))] 

print("Tempo teoria\n")
print(df_groupby)

cols = ['User', 'Time_Theory']
subset = pd.DataFrame(df_groupby, columns = cols)

#subset.to_csv("distr_Time_Theory.csv", index=False)
#######################################################################################

#filter selecting the quiz
df2 = df2[df2.Information == 'Quiz']
df2_groupby = df2.groupby(['User', 'Information', 'Month'])['Diff_Time'].sum()
df2_groupby.columns = ['User', 'Information', 'Month', 'Diff_Time']
df2_groupby = df2_groupby.reset_index()
df2_groupby = df2_groupby.rename(columns={'Diff_Time':'Time_Quiz'})


#calculate the time spent on quiz in hours
df2_groupby['Time_Quiz']=[(int)(df2_groupby.Time_Quiz[i].total_seconds()//3600) for i in range(len(df2_groupby['Time_Quiz']))] 

print("\n")
print("Tempo quiz\n")
print(df2_groupby)

cols2 = ['User', 'Time_Quiz']
subset2 = pd.DataFrame(df2_groupby, columns = cols2)

#subset2.to_csv("distr_Time_Quiz.csv", index=False)
################################################################################

#filter selecting time spent in forum
df3 = df3[df3.Information == 'Forum']
df3_groupby = df3.groupby(['User', 'Information', 'Month'])['Diff_Time'].sum()
df3_groupby.columns = ['User', 'Information', 'Month', 'Diff_Time']
df3_groupby = df3_groupby.reset_index()
df3_groupby = df3_groupby.rename(columns={'Diff_Time':'Time_Forum'})

#time spent on forum in minutes
df3_groupby['Time_Forum']=[(int)(df3_groupby.Time_Forum[i].total_seconds()//60) for i in range(len(df3_groupby['Time_Forum']))] 

print("\n")
print("Tempo forum\n")
print(df3_groupby)

cols3 = ['User', 'Time_Forum']
subset3 = pd.DataFrame(df3_groupby, columns = cols3)

#subset3.to_csv("distr_Time_Forum.csv", index=False)
###################################################################################

#filter selecting the resource which means time spent in assignment
df4 = df4[df4.Information == 'Assignment']
df4_groupby = df4.groupby(['User', 'Information', 'Month'])['Diff_Time'].sum()
df4_groupby.columns = ['User', 'Information', 'Month', 'Diff_Time']
df4_groupby = df4_groupby.reset_index()
df4_groupby = df4_groupby.rename(columns={'Diff_Time':'Time_Assignment'})

#calculate the time spent on Assignment in minutes
df4_groupby['Time_Assignment']=[(int)(df4_groupby.Time_Assignment[i].total_seconds()//60) for i in range(len(df4_groupby['Time_Assignment']))] 

print("\n")
print("Tempo assignment\n")
print(df4_groupby)

cols4 = ['User', 'Time_Assignment']
subset4 = pd.DataFrame(df4_groupby, columns = cols4)

#subset4.to_csv("distr_Time_Assignment.csv", index=False)
###################################################################################

#merge time_theory, Time_Quiz, time_forum, time_assignment

res = pd.merge(subset, subset2, how='left', on='User')
res['Time_Quiz']=res['Time_Quiz'].fillna(0)
res['Time_Quiz'] = [int(res.Time_Quiz[i]) for i in range(len(res.Time_Quiz))]

res = pd.merge(res, subset3, how='left', on='User')
res['Time_Forum']=res['Time_Forum'].fillna(0)
res['Time_Forum'] = [int(res.Time_Forum[i]) for i in range(len(res.Time_Forum))]

res = pd.merge(res, subset4, how='left', on='User')
res['Time_Assignment']=res['Time_Assignment'].fillna(0)
res['Time_Assignment'] = [int(res.Time_Assignment[i]) for i in range(len(res.Time_Assignment))]

#res.to_csv("time_analysis.csv", index=False)

