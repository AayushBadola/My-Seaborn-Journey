# edfc empirical cumulative distribution function 
# lets say there are 10 values 
# for each of those values we say val 1 -> proportion 0.1
# val 2 -> proportion 0.2
# .
# .
# .
# .
# value 10 -> proportion 1 
'''
| x  | Observations ≤ x | Percentage |
| -- | -----------------| -----------|
| 20 |                1 |        10% |
| 30 |                2 |        20% |
| 35 |                3 |        30% |
| 40 |                4 |        40% |
| 45 |                5 |        50% |
| 50 |                6 |        60% |
| 55 |                7 |        70% |
| 60 |                8 |        80% |
| 70 |                9 |        90% |
| 80 |               10 |       100% |
'''
# so based on this we can say that unlike kde (the way to find where data is concentrated) teh "EDCF" allows us to know how much of observations have been made till NOW 

# ECDF is useful when answering questions like:
# "What percentage of customers spent less than £25?"
# "What percentage of students scored below 80?"

############################################# CREATING EDCF PLOT #########################################
import seaborn as sns
import matplotlib.pyplot as plt 

tips = sns.load_dataset("tips")
sns.ecdfplot(data = tips, x="tip")
plt.show()

############################################ MIN/MAX VALUE IN THE ECDF ########################################
# we know the data / column we are using for edcf is tip so we can find the minimum and maximum tip ammount using inbuilt arguments

max_tip = tips.tip.max() # <----- max() is a built in pandas function basically we are getting a series of tips and python finds the max 
min_tip = tips.tip.min()

# it is NOT a python function since we are not doing max(data)

print(f"Max tipped value is : {max_tip}\n\n Minimum Tipped value is: {min_tip}\n\n")


########################################## FINDING HOW MANY PEOPLE / VALUE ARE IN THAT SPECIFIC DATA ############################
# we know the heading doesnt tell immediately what it is but lets try to understand 

# assume there are many people whotip and some who dont 
# so we can basically find the people who tipped what ammount 
# say 20$ -> 10 people 
# say 14$ -> 8 people 
# say 0 $ -> 2 people 

# to do this we just have to remember pandas since we know that the data here is a "data frame" we know that we can apply data frame functions to it

# we know there is a function called "value_counts" which will provide us with the above example 
# since for "tips" dataset its north of 200 rows so we will use .head() to by default limit it to 5 rows 

customer_tips = tips.tip.value_counts().head()
print(f"The Tips and the ammount of customer who tipped that ammount :\n{customer_tips}\n\n")


############################################ SETTING THE AXIS ###########################################
# here in previous chapters we were doing 
# sns.ecdfplot(data = tips, x="tip")

# this creates a graph first then opens the data finds the column "tip" and puts that columns data in x - axis 
# by default whatever axis is left that would be the proportion axis 
# we can set/ change the "tip" column to be y-axis then automatically whatever is left is taken by proportion 

sns.ecdfplot(data = tips, y="tip")
plt.show()

######################################## VERTICAL AND HORIZONTAL LINES ##########################################
# in basic mathematics we have seen that in "sin" graph if we create a vertical line from y= 1 then every point it intersects has a value of y = 1
# similarly with x axis we can do that 

# we can also do it to show sepration that is say x = 4 then we can show the sepration of data that is less than 4 and greater than 4

# to do that we can use arguments that is "axvline()" OR "ayhline()" {self explanatory but still (axvline) is "a X-axis vertical line"}

sns.ecdfplot(data = tips, x = "tip")
plt.axvline(3, color="black") # here 3 is the number / x value we want to create the vertical line on 
plt.show()

################################################# chaning the proportion to counts ######################################
# since when creating graph we were getting 2 kinds of values proportion and the column we selected 
# if we dont want the proportion but the actual count of people / count of data then we can change it 

# to change proportion to the actual count use the argument (stat='count')
sns.ecdfplot(data = tips, x = "tip", stat="count")
plt.show()


############################################### COMPLEMENTARY OF ECDF PLOT ##############################################
# complimetary is basically we plot data from last row to frist instead of first -> last

# to find the complementary of the graph we just provide "True" value to comlentary argument 

sns.ecdfplot(data = tips, x = "tip", stat="count", complementary=True)
plt.show()


############################################## APPLYING WEIGHTS #######################################################
# To sum it up (the wording it self is the answer here)
# applying weights means to tally up the results till now 
# say we have donations a 2,3,4,5,6,7
# and then proportion 0.4,0.5,0.6,0.8,0.85,0.9
# we can say at  by the time we reach 3 dollar donations we have made about 50% of of the money

 