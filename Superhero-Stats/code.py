# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading of the file
data=pd.read_csv(path)

#Code starts here 

#Replacing '-'' in the column with 'Agender'
data['Gender'].replace('-','Agender', inplace=True)

#Storing the value counts of 'Gender'
gender_count=data['Gender'].value_counts()

#Plotting bar graph of 'gender_count'
plt.bar(gender_count.index, gender_count)
plt.show()

#Storing the value count of 'Alignment' 
alignment = data['Alignment'].value_counts()

#Setting the figure size
plt.figure(figsize=(6,6))

#Plotting pie chart for 'alignment'
plt.pie(alignment,labels=alignment.index,explode=(0.05,0.05,0.05),autopct='%1.1f %%')
            
#Setting the pie chart title
plt.title('Character alignment')


#Subsetting the data with columns ['Strength', 'Combat']
sc_df = data[['Strength','Combat']].copy()

#Finding covariance between 'Strength' and 'Combat'
sc_covariance = sc_df.cov().iloc[0,1]

#Finding the standard deviation of 'Strength'
sc_strength = sc_df['Strength'].std()

#Finding the standard deviation of 'Combat'
sc_combat = sc_df['Combat'].std()

#Calculating the Pearson's correlation between 'Strength' and 'Combat'
sc_pearson = sc_covariance/(sc_combat*sc_strength)

print("Pearson's Correlation Coefficient between Strength and Combat : ", sc_pearson)


#Subsetting the data with columns ['Intelligence', 'Combat']
ic_df = data[['Intelligence','Combat']].copy()

#Finding covariance between 'Intelligence' and 'Combat'
ic_covariance = ic_df.cov().iloc[0,1]

#Finding the standard deviation of 'Intelligence'
ic_intelligence = ic_df['Intelligence'].std()

#Finding the standard deviation of 'Combat'
ic_combat = ic_df['Combat'].std()

#Calculating the Pearson's correlation between 'Intelligence' and 'Combat'
ic_pearson = ic_covariance/(ic_intelligence*ic_combat)

print("Pearson's Correlation Coefficient between Intelligence and Combat : ", ic_pearson)

#Find the quantile=0.99 value of 'Total' column
total_high= data['Total'].quantile(q=0.99)

#Subsetting the dataframe based on 'total_high' 
super_best=data[data['Total']>total_high]

#Creating a list of 'Name' associated with the 'super_best' dataframe
super_best_names=list(super_best['Name'])

#Printing the names
print(super_best_names)


