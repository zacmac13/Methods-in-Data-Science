import numpy as np
import pandas as pd

college = pd.read_csv('College.csv')
college

college2 = pd.read_csv('College.csv', index_col=0)
college2
college3 = college.rename({'Unnamed: 0': 'College'},
axis=1)
college3
college3 = college3.set_index('College')
college = college3

college.describe()

import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
columns = ['Top10perc', 'Apps', 'Enroll']
scatter_matrix(college[columns], figsize=(10, 10))
plt.show()

college.boxplot(column='Outstate', by='Private', grid=False, figsize=(10, 6))
plt.title('Distribution of Outstate Tuition by Private/Public')
plt.suptitle('')
plt.xlabel('Private')
plt.ylabel('Outstate Tuition')
plt.show()

college['Elite'] = pd.cut(college['Top10perc'],
[0,0.5,1],
labels=['No', 'Yes'])
elite_counts = college['Elite'].value_counts()
elite_counts
college.boxplot(column='Outstate', by='Elite', grid=False)
plt.title('Boxplot of Outstate by Elite Status')
plt.suptitle('') 
plt.xlabel('Elite Status')
plt.ylabel('Outstate')
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
variables = ['Outstate', 'Top10perc', 'F.Undergrad', 'S.F.Ratio']
bins_list = [10, 20, 30, 40] 
for ax, var, bins in zip(axes.flatten(), variables, bins_list):
    college[var].plot.hist(ax=ax, bins=bins, edgecolor='black')
    ax.set_title(f'Histogram of {var}')
    ax.set_xlabel(var)
    ax.set_ylabel('Frequency')
plt.tight_layout()
plt.show()

college['Apps'].mean()
college['Accept'].mean()
college['Grad.Rate'].mean()
college['Top10perc'].mean()
# I found it very interesting that these colleges had an average of over 3000 applicants per year, and accepted almost 70% of those applicants.
# I was also very surprised by how high the graduation rates were on average, sittinf north of 65%.
# Another thing I found interesting was that colleges had an average of 27.5 top 10% of high school students in their class, indicating the average size of high schools would be around 2755! WAY bigger than my high school.

boston = pd.read_csv('Boston.csv')
boston

# This dataset has 506 rows, which are 506 different suburbs of Boston. It has 14 columns which represent different things about the suburbs, including average age, pupil-teacher ratio, etc.

import seaborn as sns
sns.pairplot(boston)
plt.show

