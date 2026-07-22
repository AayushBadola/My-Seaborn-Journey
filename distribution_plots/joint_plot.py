# joint plot is used to compare 2 different plots 
# it plots a scatter plot 

import matplotlib.pyplot as plt
import seaborn as sns

######################################## CREATING JOINT PLOT (with scatter) ########################################
# since joint plot is mostly used for comparrision we need to provide x-axis and y-axis
# it is mostly used to visualize how x-data and y-data is related 

# say if we go to a restraunt and we get a really big bill then the tip should be "USUALLY" 15-20% of the total bill
# so we can then find a relationship of total bill and tips recived 

# using the sample dataset "tips"

tip_data = sns.load_dataset("tips")
sns.jointplot(
    data = tip_data,
    x = "total_bill",
    y = "tip",
    kind= "scatter"
)
plt.title("Graph with Scatter plots")
plt.show()

################################# CREATING JOINT PLOT (with kde) ################################
# when given 2 different data , which we want to compare and find relationship of , we can also do kernal density estimation 
# it provides us a "dark cloud" where most of the data is there and as the ammount of data is getting less that is less dense thus the "cloud color" also starts becoming lighter 

# EASY WAY TO REMEMBER 
# think of electron density funciton
# we know electons are not seen as individuals but as clouds of negative charges 
# more the electron the bigger and denser the cloud ,less electon more lighter the cloud 
# same concept applies here 

sns.jointplot(
    data = tip_data,
    x = "total_bill",
    y = "tip",
    kind= "kde",
    fill=True # rememebr to fill the loops otherwise seaborn will only make closed loops and you will say "you didnt tell us that"
)
plt.title("Graph with Kernal Density Estimation")
plt.show()

################################# CREATING JOINT PLOT (with hist) ################################

# when given 2 different data , which we want to compare and find relationship of ,
# we can also use histogram instead of scatter plot

# remember the histogram is NOT comparing x-data and y-data together
# it is simply showing the distribution of x-data and y-data individually

# the histogram at the TOP shows the distribution of x-axis data
# (here total_bill)

# the histogram at the RIGHT shows the distribution of y-axis data
# (here tip)

# so if most of the total bills are between 15-20 dollars
# then the top histogram will have the tallest bar around that range

# similarly if most of the tips are around 2-3 dollars
# then the right histogram will have the tallest bar around that range

# EASY WAY TO REMEMBER
# think of the center plot as answering
# "How are total_bill and tip related?"

# while the histograms answer
# "How is total_bill distributed?"
# "How is tip distributed?"

# they are just extra information provided along with the relationship plot
# so that we don't have to create two separate histograms later

sns.jointplot(
    data = tip_data,
    x = "total_bill",
    y = "tip",
    kind= "hist"
    
)
plt.title("Graph with Histograms")
plt.show()

# think of it as histogram + density

# unlike KDE, which smooths the data into a cloud,
# hist divides the graph into small rectangular bins

# each rectangle counts how many observations fall inside it

# more observations  -> darker rectangle
# fewer observations -> lighter rectangle

# therefore the center graph is actually a 2D histogram
# while the top and right graphs are normal 1D histograms

################################# CREATING JOINT PLOT (with hexagons) ###########################
# same concept as historgams having darker color for multiple data in same place 
# instead of rectangles we get hexagons 

sns.jointplot(
    data = tip_data,
    x = "total_bill",
    y = "tip",
    kind= "hex"
)
plt.title("Graph with Hexagons")
plt.show()

################################## CREATING JOINT PLOT (with regression) ################################
# think of regression as a mixture of scatter , avg patternn, line chart 
# the scatter tells us the relationship of 2 data 
# regeression tells us the patter / avg trend of that relationship 

sns.jointplot(
    data = tip_data,
    x = "total_bill",
    y = "tip",
    kind= "reg"
)
plt.show()



######################################## CUSTOMIZING THE JOINT PLOT #####################################

# same in previous modules of matplotlib we just pass the arguments given below and the choices we need to provide 
# we can do this while creating or by using the set_ command 

'''
alpha          | Controls the transparency of the plot.
               | Value   : 0.0 to 1.0

color          | Specifies the color of the plot.
               | Choices : "red", "blue", "green", "#FF5733", etc.

hue            | Groups the data by a categorical variable using different colors.
               | Value   : Column Name

palette        | Specifies the color palette used with hue.
               | Choices : "deep", "muted", "bright", "pastel",
               |           "dark", "colorblind", "Set1", "Set2",
               |           "viridis", "magma", "rocket", etc.

height         | Specifies the height of the figure.
               | Value   : Integer / Float

aspect         | Specifies the width-to-height ratio.
               | Value   : Integer / Float

col            | Creates separate Joint Plots for each category.
               | Value   : Column Name

row            | Creates separate Joint Plots for each category.
               | Value   : Column Name

fill           | Fills the KDE contours or histogram bars (where supported).
               | Choices : True / False

rug            | Displays a small tick mark for every individual observation.
               | Choices : True / False

marginal_ticks | Displays tick marks on the marginal plots.
               | Choices : True / False

space          | Controls the spacing between the joint plot and marginal plots.
               | Value   : Integer / Float

ratio          | Controls the size ratio between the joint plot and marginal plots.
               | Value   : Integer

xlim           | Sets the limits of the x-axis.
               | Value   : Tuple (min, max)

ylim           | Sets the limits of the y-axis.
               | Value   : Tuple (min, max)

'''

