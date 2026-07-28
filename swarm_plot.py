import matplotlib.pyplot as plt 
import seaborn as sns
cars = sns.load_dataset("mpg").dropna()
cars = cars[cars.cylinders.isin([4,6,8])]
# think of swarm plot as 
# SORTING -> GROUPING 
# a good analogy is 
# directors , managers , Team Leads , Employees 

# ofcoruse its mixed like Team Leads, Directors, Employees, Managers 
# so we sort it we get directors , managers , Team Leads , Employees
# and directors talk and be with directors 
# managers are with managers 
# team leads are with themselfs
# and individual contributors are with individual contributors 

#################################################### CREATING SWARM PLOTS ###########################################3
# to create a swam plot we call the funtion swarmplot
# lets say we want to create swarm based on horse power since many times there are many cars having same horse power 

sns.swarmplot(data = cars, x = "horsepower")
plt.show()

############################################## SEPRATING DIFFERENT SWARM GRAPHS BASED ON CATEGORY #######################################
# WE KNOW FOMR OUR BOX VIOLIN PLOT that we can seprate the data of show different plots based on a category like orgin 
# we can create 3 graphs like usa, japan, eu
# to do that we just have to specify our x and y axis 

sns.swarmplot(data = cars, x ="origin", y="horsepower")
plt.show()


############################################## SEPERATING THE CATEGORIES BASED ON SUB CATEGORIES ##########################################
# we did the same thing on the box violin plot where we used "hue" to create the sub category / highlight the sub category 

sns.swarmplot(data = cars, x ="origin", y = "horsepower", hue="cylinders")
plt.show()

############################################# GROUPING THE SUB CATEGORIES ############################################################
# in previous graphs we were grouping the graphs 
# 1st based on horse power 
# then we categorized them based on origin 
# then highlighted based on engine cylinders 

# now we can do something like this 

# 1st group them based on horse power 
# 2nd group them based on origin 
# 3rd hgihlight the engine cylinders 
# 4th group each of the highlighted cylinders 

# so for USA it groups V4 , V6 , V8 
# similarly for EU and japan 
# for doing this we just make the "dodge" argument true 

sns.swarmplot(data = cars, x = "origin", y = "horsepower", hue = "cylinders", dodge = True)
plt.show()

######################################## OVERLAYING SWARM PLOTS ON TOP OF BOX PLOTS ######################################
# we know that box plots are basically visual representaion of more asthetic representation of swarm plots 
# and we can see that by overlaying those on top of box plots 
# to do that we just have to apply the concept of displaying multiple graphs we learned in matplotlib 
# basically construct graph1 
# constact graphs 2 
# then call plt.show()

# dont do graph 1 -> plt show -> graph 2 -> plt show 
# we are doing -> graph 1 -> graph 2 -> show both 

# lets take example of USA and dividing it based on cylinders 

usa = cars[cars.origin == "usa"]

# box plot 
sns.boxplot(data = usa, x = "origin", y="horsepower")
# swarm plot
sns.swarmplot(data = usa, x = "origin", y="horsepower")
# displaying both of them
plt.show()

########################################## OVERLAYING ON TOP OF VIOLIN ######################################
# same thing since violin is just box + kde we can overlay the swarm plot on top of violin using the same concept 
