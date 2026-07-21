import seaborn as sns
# Seaborn is built on top of Matplotlib.
# It uses Matplotlib internally to draw all the graphs.

# Seaborn is NOT built on top of Pandas.
# However, it is designed to work extremely well with Pandas DataFrames.

# We generally use Pandas to:
# - read the data
# - clean the data
# - analyze the data

# Then we pass that DataFrame to Seaborn.

# Seaborn automatically communicates with Matplotlib to draw the graph.

# So a typical workflow is:
'''
                    ┌──────────────────────────────┐     ┌─────────────────────────┐     ┌────────────────────────────┐
                    │ Pandas                       │ ──► │ Seaborn                 │ ──► │ Matplotlib                 │
                    │ • Read Data                  │     │ • Choose Visualization  │     │ • Actually Draws Graph     │
┌─────────────┐     │ • Clean Data                 │     │ • High-Level Interface  │     │ • Rendering Engine         │
│ CSV / Excel │ ──► │ • Analyze Data               │     │ • Works with DataFrames │     └────────────────────────────┘
└─────────────┘     └──────────────────────────────┘     └─────────────────────────┘ 
'''  

######################################## IMPORTING DATA USING SEABORN #################################

# Usually, we use Pandas to import datasets from files such as CSV, Excel, JSON, etc.

# Seaborn also provides sns.load_dataset(), but it is ONLY used to load
# built-in sample datasets (like tips, iris, penguins, flights, etc.).

# It does NOT replace pd.read_csv(), pd.read_excel(), etc.

# The object returned by sns.load_dataset() is a Pandas DataFrame. 

###### IN SHORT BASICALLY YOU WANT YOU OWN DATASET TO USE -> NUH UH YOU CANT JUST IMPORT IT USING SEABORN YOU HAVE TO USE "PANDAS"

'''
⡴⠒⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠉⠳⡆⠐
⣇⠰⠉⢙⡄⠀⠀⣴⠖⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⠉⠙⡆
⠘⡇⢠⠞⠉⠙⣾⠃⢀⡼⠀⠀⠀⠀⠀⠀⠀⢀⣼⡀⠄⢷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠰⠒⠲⡄⠖⣏⣆⣀⡍
⠀⢠⡏⠀⡤⠒⠃⠀⡜⠀⠀⠀⠀⠀⢀⣴⠾⠛⡁⠀⠀⢀⣈⡉⠙⠳⣤⡀⠀⠀⠀⠘⣆⠀⣏⡼⢋⠀⠀⢱
⠀⠘⣇⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⡴⢋⡣⠊⡩⠋⠀⠀⠀⠣⡉⠲⣄⠀⠙⢆⠀⠀⠄⣸⠀⢉⠀⢀⠿⠀⢸
⠀⠀⠸⡄⠀⠈⢳⣄⡇⠀⠀⢀⡞⠀⠈⠀⢀⣴⣾⣿⣿⣿⣿⣦⡀⠀⠀⠀⠈⣧⠌⠀⢳⣰⠁⠀⠀⠀⣠⠃
⠀⠀⠀⠘⢄⣀⣸⠃⠀⠀⠀⡸⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠂⠉⣇⠀⠀⠙⢄⣀⠤⠚⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⢘⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⢰⣿⣿⣿⡿⠛⠁⠀⠉⠛⢿⣿⣿⣿⣧⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⣸⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡀⢀⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡇⠹⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡿⠁⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣤⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⣀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⢤⣀⣀⠀⢀⣀⣀⠤⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''

# the built in data sets are 

'''
sns.load_dataset("tips")
sns.load_dataset("iris")
sns.load_dataset("penguins")
sns.load_dataset("titanic")
sns.load_dataset("flights")
sns.load_dataset("diamonds")
sns.load_dataset("exercise")
sns.load_dataset("fmri")
sns.load_dataset("mpg")
sns.load_dataset("car_crashes") <-------- WE WILL USE THIS DATASET FROM NOW ON 
sns.load_dataset("planets")
sns.load_dataset("dots")
sns.load_dataset("attention")
sns.load_dataset("anagrams")
sns.load_dataset("brain_networks")
sns.load_dataset("healthexp")

'''
# Want to see all available built-in datasets?
# print(sns.get_dataset_names())

# we can use the "sample dataset" by loading it and "saving" it or "storing" it in a variable 

crashes = sns.load_dataset("car_crashes")
print(f"ONLY THE SAMPLE DATASET WHICH IS INSIDE THE SEABORN CAN BE LOADED BY USING \"sns.load_dataset()\" :\n{crashes}\n\n")

####### IMPORTANT NOTICE: IF DATASET IS BIG USE CRASHES.head() since printing crashes will print the ENTIRE dataset 
# the crashes.head() will print the first 5 rows 
# we can specify how many rows we do want to see by using crashes.head(rows we want to see)



## we can also see the last rows by using tail() or by specifiying how many last orws we want to see 


print("-------------------- TO USE OTHER DATASETS WHICH IS NOT IN SEABORN USE PANDAS --------------------")