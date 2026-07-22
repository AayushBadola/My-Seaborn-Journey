# A distribution plot is used to visualize how data values are distributed.

# It helps us understand:
# - Where most of the data is concentrated (peak)
# - How spread out the data is (dispersion)
# - Whether the data is symmetric or skewed
# - Whether the data has one peak (unimodal) or multiple peaks (multimodal)

# LEFT SKEWED  -> Long tail towards the left.
# RIGHT SKEWED -> Long tail towards the right.

# provides us insight if data has multiple peaks(has sub groups) or a single peak


# INTERPRETING A DISTRIBUTION PLOT
#
# X-axis -> Data values
# Y-axis -> Frequency (number of observations in each bin)
#
# Taller bars indicate that more observations fall within that range.

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
##################################### CREATING DISTRIBUTION PLOT #####################################
# we can create a distribution plot simply by calling "sns.displot(data)"
data = np.random.normal(loc= 60, scale=5, size=200)

sns.displot(data)

plt.show() # since seaborn is built on top of matplot we have o use matplot "plt.show()" to actually show the graph built by seaborn

#################################### ADDING kernal Density Estimation to DISTRIBUTION PLOT #############################
# Kernel Density Estimation (KDE) is a smooth continous curve used to estimate the probability density function 
# unlike the rugged bins of histogram its much smoother 

# KDE is an optional density estimate that Seaborn can calculate and overlay
# on top of the histogram by setting kde=True.

sns.displot(data, kde=True)
plt.show()

######################################## USING IMPORTED DATA FOR DISTRIBUTION PLOT #####################################
crashes = sns.load_dataset("car_crashes")

# say we want to do distribution plot based on a specific column then we just access that column like we access a dataframe 

sns.displot(crashes["not_distracted"]) # selecting columns or car crashes where driver were not distracted 
plt.show()

#################### WE CAN NOT SHOW RELATIONSHIPS IN DISTRIBUTION PLOT AS ITS A UNIMODAL SO IT SHOWS THE DATA OF ONLY 1 CATEGORY 


###################################### CUSTOMIZATION FOR DISPLOTS ####################################################

'''
kind           | Specifies the type of distribution plot.
               | Choices : "hist" (Default), "kde", "ecdf"

bins           | Specifies the number of histogram bins.
               | Value   : Integer (Ex : 10, 20, 30)

binwidth       | Specifies the width of each histogram bin.
               | Value   : Integer / Float (Ex : 2, 5, 10)

binrange       | Specifies the range over which bins are created.
               | Value   : Tuple (min, max)
               | Example : (0, 100)

rug            | Displays a small tick mark for every individual data point.
               | Choices : True / False

color          | Specifies the color of the plot.
               | Choices : "red", "blue", "green", "#FF5733", etc.

hue            | Groups the data using different colors.
               | Value   : Column Name

palette        | Specifies the color palette used with hue.
               | Choices : "deep", "muted", "bright", "pastel",
               |           "dark", "colorblind", "Set1", "Set2",
               |           "viridis", "magma", "rocket", etc.

height         | Specifies the height of the figure.
               | Value   : Integer / Float

aspect         | Specifies the width-to-height ratio.
               | Value   : Integer / Float

col            | Creates separate plots for each category.
               | Value   : Column Name

row            | Creates separate plots for each category.
               | Value   : Column Name

multiple       | Controls how multiple distributions are displayed.
               | Choices : "layer" (Default), "stack", "fill", "dodge"

element        | Specifies the histogram style.
               | Choices : "bars" (Default), "step", "poly"

fill           | Specifies whether the bars/KDE curve should be filled.
               | Choices : True / False

alpha          | Controls the transparency.
               | Value   : 0.0 to 1.0

stat           | Specifies what the histogram displays.
               | Choices : "count" (Default), "frequency",
               |           "density", "probability", "percent"

common_norm    | Specifies whether all hue groups share normalization.
               | Choices : True / False

common_bins    | Specifies whether all hue groups use the same bins.
               | Choices : True / False

'''






