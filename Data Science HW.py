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
# This plot shows a HUGE variability throughout all 506 cities we'll be analyzing. Crime rates, accessibility to highways, pupil-teacher ratios in school, and retail industries all have incredibly good numbers in some cities, but horrible numbers in other cities. This shows me that the data is not skewed, and that it is correct information taken without heavy bias to the area of Boston.

correlation_with_crim = boston.corr()['crim'].sort_values(ascending=False)
print("Correlation with per capita crime rate (CRIM):")
print(correlation_with_crim)
# The crime has the highest correlation with accessibility to radial highways (rad), which makes sense because the criminals would have an easy out. Taxes are a close second, though, as they also correlate strongly with crime rates. Columns like age, indus, or pratio, on the other hand, don't have a large impact on crime rates

high_crime_rate = boston[boston['crim'] > boston['crim'].mean()]
high_tax_rate = boston[boston['tax'] > boston['tax'].mean()]
high_pupil_teacher_ratio = boston[boston['ptratio'] > boston['ptratio'].mean()]

print(f"Number of suburbs with high crime rate: {high_crime_rate.shape[0]}")
print(f"Number of suburbs with high tax rate: {high_tax_rate.shape[0]}")
print(f"Number of suburbs with high pupil-teacher ratio: {high_pupil_teacher_ratio.shape[0]}")
# 128 of these Boston counties have high crime rates, which is over one quarter of the counties in question. In general, I'm seeing that Boston and the surrounding areas are not super safe places.
# Even more of these counties have high tax rates, north of 30%! This isn't surprising, though, as Boston is a large city and there is a lot to pay for downtown.
# More than half of these Boston school districts report high pupil-teacher ratios, giving a third strike to living in the Boston area. If I was planning to move, I would look for an alternate city.
 
charles_river_count = boston[boston['chas'] == 1].shape[0]
print(f'There are {charles_river_count} suburbs that border the Charles River')

median_pupil_teacher_ratio = boston['ptratio'].median()
print(f'The average pupil-teacher ratio is {median_pupil_teacher_ratio}')

lowest_value_suburb = boston.loc[boston['medv'].idxmin()]
print(lowest_value_suburb)
# This city that has the lowest median value also has very high taxes, little access to highways, and a lot of crime. This is not a city I would like to reside in. It also looks like this city has a large population in a small space as well as a lot of factories, or non-retail business. This is likely an area right outside downtown Boston that would be considered the "hood". You get these in all big city outskirts.

more_than_seven_rooms = boston[boston['rm'] > 7].shape[0]
more_than_eight_rooms = boston[boston['rm'] > 8].shape[0]
print(f'Number of suburbs averaging more than seven rooms: {more_than_seven_rooms}')
print(f'Number of suburbs averaging more than eight rooms: {more_than_eight_rooms}')

suburbs_with_more_than_eight_rooms = boston[boston['rm'] > 8]
print("Suburbs averaging more than eight rooms:")
print(suburbs_with_more_than_eight_rooms)
# While there are outliers, most of these cities have low crime rates and heavy retail industry. The average age of these cities is also very high, two of them even being north of 90 years old! These are more likely nicer cities with older folks that have more money to spend on nicer houses.