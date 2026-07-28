# in previous plots we specified the parameters beased on a single type OR comparing and finding relationships of 2 types using joint plots 
# a pair plot by itself finds all the replationships by it self
# FOR example the dataset we are going to use is based on "tips"
# the headers of "tips" dataset is 
# total_bill
# tip
# sex
# smoker
# day
# time
# size

# the plot automatically generates every possible pair
# between the numerical columns
#
# for example
# total_bill vs tip
# total_bill vs size
# tip vs size

################################################# CREATING PAIR PLOTS ######################################################
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

sns.pairplot(tips)
plt.show()

# pair plot is showing histograms on diagonal 
# pair plot is showing scatter plots on Non-Diagonals

# we can customize what the pair plot shows by using the argument "Kind"

################################################## CHANGING GRAPH KIND ON NON-DIAGONALS ######################################
# we can customize what the pair plot shows by using the argument "Kind"
# by default it will change the graph on non - diagonals 

#### NON DIAGONAL REGRESSION
sns.pairplot(tips, kind="reg")
plt.show()

#### NON DIAGONAL KERNAL DENSITY ESTIMATION
sns.pairplot(tips, kind="kde")
plt.show()
############## IMPORTANT NOTICE #############:
# by doing sns.pairplot(tips, kind="kde", fill=True)
# basically doing the customization arguments that wont work for pairplot()
# as pair plot is basically a high level wrapper 
# internall its doing PairGrid.map_offdiag(sns.kdeplot)
# so we pass our customization as a dict and it unpacks it internally and passes the actual arguments to kdeplot 
# use the argument "plot_kws"

################################################ CHANGING GRAPH KIND ON "DIAGONALS" ############################################
# for changing the type of graph displayed on diagonals we can use the argument "diag_kind" whcih will change the diagonal kind 
# the types which are allowed is same as that for normal "kind"(reg, hex, hist, kde)

sns.pairplot(tips, diag_kind="hist", kind="kde", diag_kws={"color" : "Blue"}  , plot_kws={"fill" : True}) # non diagonal are kde and diagonal are regression 
plt.show()

################################################ ADDING ON TO THE ORIGINAL PLOTS ###############################################

# basic mathematics time !
# in matirces we learn about upper triangle and lower triangle as well as diagonals 
# now when we add on to the original plots created we use some arguments like "map_upper()" and "map_lower()"
# this will apply / add the new graphs on top of the lower OR upper triangle 

# after using map_upper or map_lower we can then pass the plots nad colors and specifications we want to update / show on top 
# FOR USING THIS WE NEED TO USE A PAIR GRID (the thing pairplot returns) if we store our data its a DATA FRAME

# pair plot is symmetric
# therefore the upper and lower triangles contain the same information

# by using corner=True
# seaborn only displays the lower triangle
# making the plot cleaner and easier to read


data = sns.pairplot(tips)

data.map_upper(sns.kdeplot, levels=6, color="Red")
plt.show()

############################################### PAIR PLOTS WITH SPECIFIC CATEGORIES ############################################
# for any pairplot pairgraph we have multiple graphs there we can select a condition say weekend = True
# as we know in pair plot there are multiple graphs (say Main graph) 
# in that main graph there are multiple graphs lets call those "sub plots"
# now by attaching a <condition> in "hue" we will create 2 graphs which overlap for that sub graph in which the graphs will be on with weekend is false and another where its true 

# so in a single subgraph there are 2 graphs with different colors showing condition = false and condition = true 

#### for this we use the argument "hue"

sns.pairplot(tips, hue="day")
plt.show()

# we can see that for everyday there is a graph in "subgraph"

########################################## HAVING SPECIFC GRAPHS IN PAIR PLOT ####################################################
# we know in pair plot it generates multiple sub plots which form a gird
# if we dont want to have multiple plots having multiple comparisions we can select the comparisions we want  

# we can provide the X axis datas by usign the argument x_vars = ["col1", "col3", "col8"] OR y_vars = ["col2", "col5"]
# after doing that the seaborn will only use the data for x and y axis that we have provided 

sns.pairplot(tips, x_vars=["tip"], y_vars=["total_bill", "size"], kind="reg")
plt.show()

