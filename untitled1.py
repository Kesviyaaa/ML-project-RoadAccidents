# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lqy8_YSVVf7152W60F5GUKmfhtB8bkLh
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('/content/monroe county car crach 2003-2015.csv', encoding='latin-1')

data.head(10)

data.tail(10)

data.shape

data.size

data.describe()

data.columns

data.index

data.isnull().sum()

sns.heatmap(data.isnull(),cmap  ='viridis',cbar=False)

data['Weekend?'].unique()

data['Weekend?'] =data['Weekend?'].map({'Weekday':0,'Weekend':1})

data['DayOfWeek'] = pd.to_datetime(data[['Year','Month','Day']]).dt.day_name()

plt.figure(figsize=(10,6))
sns.countplot(x=  'DayOfWeek',data=data,order= ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
plt.title('Crashes by Day of Week')
plt.show()

plt.figure(figsize=(20,6))
sns.countplot(x = 'Hour',data=data)
plt.title('Crashes by hour')
plt.xlabel("Hour of the Day")
plt.show()

plt.scatter(data['Longitude'],data['Latitude'],alpha =0.5)
plt.title('Geospatial Distribution of crashes')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()

plt.figure(figsize=(20,6))
sns.countplot(x = 'Hour',data=data)
plt.title('Crashes by hour')
plt.xlabel("Hour of the Day")
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(x = 'Collision Type',data= data)
plt.title('Distribution of Collision Types')
plt.xticks(rotation = 45)
plt.show()

plt.figure(figsize = (10,6))
sns.countplot(x ='Injury Type',data=data)
plt.title('Distribution of Injury Types')
plt.xticks(rotation = 90)
plt.show()

plt.figure(figsize=(10,6))
sns.countplot(x = "Primary Factor",data=data)
plt.title('Distribution of primary factors')
plt.xticks(rotation =90)
plt.show()

numerical_columns = data.select_dtypes(include=['float64', 'int64']).columns
numerical_data = data[numerical_columns]

correlation_matrix = numerical_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix of Numerical Features')
plt.show()