#!/usr/bin/env python
# coding: utf-8

# # Introduction:
# 
# California housing data set, which contains data drawn from the 1990 U.S. Census. The following inormation provides descriptions,data types for each feature in the data set.
# 
# ***FEATURE**	                      **DESCRIPTION**	                                         **DATA TYPE**                                
# ----Longitude	      A measure of how far west a house is; a more negative value is farther west--Continuous data	
# 
# ----Latitude	      A measure of how far north a house is; a higher value is farther north--continuous data	
# 
# ----HousingMedianAge  Median age of a house within a block; a lower number is a newer building--continuous data	
# 
# ----TotalRooms	      Total number of rooms within a block--Discrete	
# 
# ----TotalBedrooms	  Total number of bedrooms within a block--Discrete	
# 
# ----Population	      Total number of people residing within a block--Discrete	
# 
# ----Households	      Total number of households, a group of people residing within a home unit, for a block--Discrete	
# 
# ----MedianIncome	  Median income for households within a block of houses --Continuous data	
# 
# ----MedianHouseValue  Median house value for households within a block --Discrete
# 
# ----OceanProximity    Distance of the house from ocean/sea--Nominal
# 
# 
# In this sample a block group on average includes 1425.5 individuals living in a geographically compact area.The final data contained 20,640 observations on 9 characteristics.
# 

# In[5]:


import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
# import required libraries for reading & graphical representaion of data


# In[9]:


import pandas as pd
housing=pd.read_excel('housing.xlsx')
# using pandas to read the data file which is an excel file
housing.head() 
# head is used for read first five records


# In[7]:


housing.info()


# Observation:-
# 1--The above data shows total 20640 entries. 
# 2--shows default indexing i,e 0 to 20639. 
# 3--shows total 10 column for different parameters. 
# 4--all data vlaue are numerical float type except ocean_proximity which is text 
# 5--type i,e object. 
# 6--total_bedrooms column has 207 null values/missing values. 
# 7--total memory usage is 1.6+ MB.

# Q.1 What is the average median income of the data set and check the distribution of data using appropriate plots. Please explain the distribution of the plot.

# In[18]:


income_mean = housing['median_income'].mean() 
print(income_mean)
# calculated medain income mean and stored it in a variable as income_mean
income_median = housing['median_income'].median() 
print(income_mean)
# calculated medain income mean and stored it in a variable as income_mean


# In[39]:


plt.hist(housing.median_income, color='blue')
plt.xlabel("median_income")
plt.title("median_income")
#using density histogram plot to see the skewness in data as density plot is modified verion of histogram


# Q.2 Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.

# In[20]:


plt.hist(housing["housing_median_age"],color='pink')  #Histogram is used to see the distribution of a numerical value.
plt.title("housing_median_age- Histogram plot")    # x-axis=housing_median_age,y-axis=Frequencies
plt.xlabel("housing_median_age")
plt.ylabel("Frequencies")
plt.grid(True)
plt.show()


# Observation:- From the above histogram plot we can come to the analysis that it is distributed symmetrically. frequency is highest at the age of 35.

# Q.3 Show with the help of visualization, how median_income and median_house_values are related?

# In[21]:


sns.scatterplot(x="median_house_value",y="median_income",data=housing)
 ##scatter plot gives a relation between two numerical values.
 #x-axis median_house_value  #Y axis median_income


# Observation:- 1.From the above observation it is to be analysed that with an increase in the median_house_value there is also an increase in the median income. 
# 2.Outlier is present in median_house_value which is shown in the graph, Therefore,median_house_value is directly proportional to median income.

# Q.4 Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available.

# In[22]:


housing[housing.isnull().any(axis=1)]
#The isnull() method returns a DataFrame object where all the values are 
#replaced with a Boolean value True for NULL values, and otherwise False.
#Here missing values are denoted by NaN


# Observation:- 1.In the above code,missing values are identified by using isnull()method.
# 2.This missing values are identified in the column 'total_bedrooms' and the mising values is denoted by NAN.

# Q.5 Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.

# In[23]:


housing["total_bedrooms"]=housing["total_bedrooms"].fillna(housing['total_bedrooms'].mean())
housing


# Observation:- 1.In the above code,a new dataset had been created where the missing values in the 'total_bedrooms'which are denoted by NaN are replaced with the mean value of the 'total_bedrooms'.

# Q.6 Write a programming construct (create a user defined function) to calculate the median value of the data set wherever required.

# In[24]:


housing.median() 


# Q.7 Plot latitude versus longitude and explain your observations.

# In[25]:


sns.scatterplot(x='latitude',y='longitude',data=housing)  
#Scatter plot gives a relationship between two numerical values.
 #x-axis = latitude #y-axis = longitude


# Obervation:- From the above plot,it is to be noted that with an decrease in longitude,latitude is increased.From this point of view,it is to be known that latitude and longitude are not dependent on each other.From this we can say that longitude is inversely proportional to latitude

# Q.8 Create a data set for which the ocean_proximity is ‘Near ocean’.

# In[28]:


near_by_ocean=housing.loc[housing["ocean_proximity"]=="NEAR OCEAN"] 
# loc is an label based method which is used to select rows and columns by Names/Labels.
print(near_by_ocean)


# Obervation :- A data set is created were ocean proximity is near ocean

# Q.9 Find the mean and median of the median income for the data set created in question 8.

# In[33]:


near_by=near_by_ocean['median_income'].mean() #getting mean of near_by as created in Q.8
near_by1=near_by_ocean['median_income'].median() #getting medain of near_by as created in Q.8
print(near_by)
print(near_by1)


# Observation:- The mean and median value of the 'median_income'in the created new dataset are:4.005784 and 3.64705 respectively.

# 10.Please create a new column named total_bedroom_size. If size 10 or less. It should be quoted as small. If the size is 11 or more but 1000 less, it should be medium, otherwise it should be large.

# In[34]:


total_bedroom_size=[]
for room in housing['total_bedrooms']:
    if room<=10:
        total_bedroom_size.append(['small'])
    elif room>=11 and room<=1000:
        total_bedroom_size.append(['medium'])
    else:
        total_bedroom_size.append(['large'])
housing['total_bedroom_size']=total_bedroom_size
housing['total_bedroom_size']     
        


# In the above data set a new column named total_bedroom_size had been added.Where the total_bedroom_size had been compared to the total_bedrooms while mentioning about the sizes of the total_bedroom_size,where:
# 1--If the total_bedroom_size <=10 it is indicated as "small" If the total_bedroom_size >=11 or <=1000 it is indicated as "medium" If the total_bedroom_size >1000 it is indicated as "large"
# 
# Conclusion
# 
# 1.All the features present in this dataset are of float type except ocean_proximity which is of object datatype,
# 
# 2.plot between median_income vs median_house_values is directly proportional to each other as it has positive correlation.
# 
# 3.plot between latitude and longitude is inversely proportional to each other as within increase in latitude,there is decrease in longitude.Therefore ,it has a negative correlation.
