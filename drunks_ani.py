# -*- coding: utf-8 -*-
"""
"""

# import packages
import matplotlib.pyplot as plt
import matplotlib.animation
import drunkframework
import pandas as pd
import sys

# system args
num_of_iterations = int(sys.argv[1])

# read in environment as a list of lists
environment = []
with open('drunk.plan.txt', 'r') as file_for_reading:
    for row in file_for_reading:
        rowlist = row.split(',')
        rowlisty = list(map(int, rowlist))
        environment.append(rowlisty)
        

# visualize the environment
maxy = len(environment[1])
maxx = len(environment) 
'''
plt.xlim(0, maxx)
plt.ylim(0, maxy)
plt.imshow(environment)
'''
                    
# locate pub in environment as values of 1 are not distinguishable on plot
df = pd.read_csv('drunk.plan.txt')
pub_rows = []
pub_cols = []
for row in range(df.shape[0]): 
         for col in range(df.shape[1]):
             if df.iat[row,col] == 1:
                 pub_rows.append(row)
                 pub_cols.append(col)

#print(min(pub_rows),np.mean(pub_rows), max(pub_rows))
#print(min(pub_cols),np.mean(pub_cols), max(pub_cols))

plt.xlim(0, maxx)
plt.ylim(0, maxy)
plt.imshow(environment)
plt.scatter(pub_cols, pub_rows)       
plt.show()       

# negate values of homes
for row in environment:
    for i, item in enumerate(row):
       if item > 1:
           row[i] = -1*item

maxy = len(environment[1])
maxx = len(environment) 
plt.xlim(0, maxx)
plt.ylim(0, maxy)
plt.imshow(environment)

'''
env_df = pd.DataFrame(environment)
env_df.max()
env_df.to_csv('env_df.csv')
'''

# Initialize variables
drunks = []
drunk_names = list(range(-10, -260, -10))
carry_on = True
fig = plt.figure(figsize=(7, 7))    
ax = fig.add_axes([0, 0, 1, 1])


# find drunks homes
df = pd.DataFrame(environment)
counter = 0
drunken = []
home_rows = []
home_cols = []
for row in range(df.shape[0]): 
         for col in range(df.shape[1]):
             for name in drunk_names:
                 if df.iat[row, col] == name:
                     drunken.append(name)
                     home_rows.append(row)
                     home_cols.append(col)
                     drunk_names.remove(name)
             
# make drunks
drunks = []
for i in range(len((drunken))):
    drunks.append(drunkframework.Drunk(environment, drunken[i], home_rows[i], home_cols[i]))


# update function
def update(misc):

    fig.clear()  
    global carry_on
    global counter 
    global num_of_iterations

    for drunk in drunks:          
        if environment [drunk.y][drunk.x] == drunk.name:
            drunks.remove(drunk)
        elif environment [drunk.y][drunk.x] > -1:
            drunk.steps()
            drunk.move()           
        else:
            drunk.move()
    
    counter += 1
    if counter == (num_of_iterations):         
        for drunk in drunks:
            drunk.go_home()
        carry_on = False

    
    if len(drunks) == 0:
        carry_on = False
        print("Stopping condition met - all drunks home!")           
    
    # overlay drunks on plot of environment
    plt.xlim(0, maxx)
    plt.ylim(0, maxy)
    plt.imshow(environment)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.title('Drunks')  
    
    for drunk in drunks:
        plt.scatter(drunk.x, drunk.y, s=50, c = 'white', label = 'drunks') 
    

# generator function to supply data to update function and each frame of animation
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < 100000000000) & (carry_on) :
        yield a
        a = a + 1


# animation 
animation = matplotlib.animation.FuncAnimation(fig, update, interval = 10, frames=gen_function)
plt.show()



'''
for i in range(num_of_iterations):
    for drunk in drunks:          
        #for j in range(num_of_iterations):
        #while environment [drunk.y][drunk.x] != drunk.name:
        if environment [drunk.y][drunk.x] == drunk.name:
            #print('someone found his home alright')
            continue
        elif environment [drunk.y][drunk.x] >=0:
            drunk.move()
            #drunk.steps()
        else:
            drunk.move()

plt.xlim(0, maxx)
plt.ylim(0, maxy)
plt.imshow(environment)

for drunk in drunks:
    plt.scatter(drunk.x, drunk.y, s=50, c = 'white', label = 'drunks') 


'''




'''

# 4. Save the density map to a file as text.
with open('environment.density.txt', 'w', newline='') as f:
    csvwriter = csv.writer(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
    for row in environment:
        csvwriter.writerow(row)
        
'''