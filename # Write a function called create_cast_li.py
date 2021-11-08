# Write a function called create_cast_list that takes a filename as input and returns a list of actors' names. 
import pandas as pd
def create_cast_list(filename):
    cast_list = []
    with open(filename,'r') as f :
    #use the for loop syntax to process each line
        for line in f :
            name = line.strip().split(',')[0]
    #and add the actor name to cast_list
            cast_list.append(name)
    return cast_list

cast_list = create_cast_list('C:/Users/akshay/Desktop/cAPEGEMINI/filename.txt')
for actor in cast_list:
    print(actor)
p= pd.DataFrame(cast_list,columns=["Name"])
print(p)
