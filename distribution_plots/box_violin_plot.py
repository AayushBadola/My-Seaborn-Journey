import matplotlib.pyplot as plt 
import seaborn as sns


# box plot is basically the visual information of 5 number summary 
# a box plot visually represents the data in this order 
# minimum value 
# 1st quatertile
# median 
# 3rd quatertile
# maximum value 

# so its basically this 

#  Minimum       Lower            Median             Upper       Maximum
#     .          Whisker             .              Whisker         .
#     .             .                .                .             .
#     |-------------|================|================|-------------|
#                   Q1               |               Q3
#                                    |
#                                 Median
#
#          <--------- Interquartile Range (IQR) --------->


# before we begin here is a cleaning method from pandas 
#################################### ISIN() ####################################

# isin() checks whether each value belongs
# to a given list (or collection).

# It returns True for matching values
# and False otherwise.

# Mostly used for filtering rows.

# Example:
# tips["day"].isin(["Sat", "Sun"])

# Meaning:
# "Is the day either Saturday or Sunday?"

# Equivalent to:
# (tips["day"] == "Sat") | (tips["day"] == "Sun")


############################################### CREATING BOX PLOT ##############################################
# for creating a box plot we just have to use a funciton called "sns.boxplot()"
cars = sns.load_dataset("mpg")
# the columns for this dataset is 
# mpg  (miles per gallon)
# cylinders  
# displacement  
# horsepower  
# weight  
# acceleration  
# model_year 
# origin
# name

# from our data we know that most people use V6 , V8, V4 so we will filter them so that we are only using those engines

cars = cars[cars.cylinders.isin([4,6,8])]
sns.boxplot(data = cars, x = cars.mpg) # finding the data for miles per gallon
plt.show()


## we can also get the actual data that is shown by using describe 
# think of describe as conversion of visible plot data to actual numerical data 

print(f"Box plot summary:\n{cars.mpg.describe()}")

####################################### CREATING MULTIPLE BOX PLOTS FOR DIFFERENT CATEGORICAL DATA #######################################
# say we know in our data its seprated by origins as well 
# if our manager says "Hey our fav 10X engineer we need to find teh 5 summary values for cars made in japan , us , europe"
# then we wont create different box plots by doing .mpg and individually doing isin = (["EU"])
# we can by default categorize our data just by providing specific x and y values 
# we want to seprate by origin so our x become the origin col 
# we want the values in y axis so our mpg col becomes Y 

sns.boxplot(data = cars, x = cars.origin, y  = cars.mpg)
plt.show()

# each box now represents one category.

# therefore,
# every origin (USA, Europe, Japan)
# gets its own Five-Number Summary.

# this makes it easy to compare
# the distributions between different categories.

################################################### SUB DIVIDING DATA USING HUE ####################################
# we know that our data is divided into many things 2 most important are number of cylinders and maker origin 
# we have the capability to have multiple sub box plots by setting a standard value to compare that is providing the column 
# we can now sub divide the plot by using hue which will divide it into 2 categories 

# box plot 
#        |
#        |--- Countries 
#                   |
#                   |------ NUMBER OF CYLINDERS 

# so first the graph is divided based on the cols we select as axis
# then it is sub divided based on the hue 
# basically USA -> v4, v6 , v8 
# japan - v4, v6, v8 
#  EU   - v4, v6, v8

sns.boxplot(data = cars, x= cars.origin, y = cars.mpg, hue=cars.cylinders)
plt.show()


#################################### VIOLIN PLOT ####################################

# think of a violin plot as

# BOX PLOT
# +
# KDE (Kernel Density Estimation)

# therefore,
# it not only shows the statistical summary
# (median, quartiles, IQR)

# but also shows where the data is concentrated
# by displaying the KDE curve.

# EASY WAY TO REMEMBER

# Box Plot   -> Statistical Summary

# KDE        -> Distribution Shape

# Violin Plot -> Box Plot + KDE