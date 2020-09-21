# house list of lists
#for loop of list


house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for index, h in enumerate(house): 
    print("the " + h[0] + " is " + str(h[1]) + " sqm")

#for loop of dictionary 
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)

#If you're dealing with a 1D Numpy array, looping over all elements can be as simple as:

for x in my_array :
    ...

#If you're dealing with a 2D Numpy array, it's more complicated. A 2D array is built up of multiple 1D arrays. 
# To explicitly iterate over all separate elements of a multi-dimensional array, you'll need this syntax:

for x in np.nditer(my_array) :
    ...
Two Numpy arrays that you might recognize from the intro course are available in your Python session: np_height, 
a Numpy array containing the heights of Major League Baseball players, and np_baseball, a 
2D Numpy array that contains both the heights (first column) and weights (second column) of those players.

# Import numpy as np
import numpy as np

# For loop over np_height
for x in np_height :
    print(str(x) + " inches")

# For loop over np_baseball
for x in np.nditer(np_baseball) :
    print(x)


#Loop over DataFrame (1)
Iterating over a Pandas DataFrame is typically done with the iterrows() method. Used in a for loop, every observation is iterated over 
and on every iteration the row label and actual row contents are available:

for lab, row in brics.iterrows() :
    ...
In this and the following exercises you will be working on the cars DataFrame. It contains information on the cars per capita and 
whether people drive right or left for seven countries in the world.


# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)
print(cars)
# Iterate over rows of cars
for x, row in cars.iterrows():
    print(x)
    print(row)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": "  + str(row['cars_per_cap']))

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
    
# Print cars
print(cars)

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)