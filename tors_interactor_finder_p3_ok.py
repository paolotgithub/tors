import csv
import sys
import time
import datetime

###

# SEARCH FOR THE INTERACTORS, CREATES THE INTERACTOME AND THE LIST OF INTERACTORS

# by Paolo Tieri, CNR, paolo.tieri@cnr.it, 2017-2021

# ported from Python 2  to Python 3 on May 2021

###

### print instructions

print('\n'+"###########################################################################################"+
        '\n'+"# TORS SEARCHES FOR BINARY INTERACTION IN PPI DATASETS STARTING FROM A LIST OF SEED GENES #"+'\n'+
        "###########################################################################################"+'\n'+'\n'+
        "* * * * * * *"+'\n'+'\n'+
        "Instructions:"+'\n'+'\n'+
        "Step 1: enter the file name of the PPI dataset containing all interaction pairs,"+'\n'+
        "the dataset must be at least two columns (interactor A - interactor B) and" +'\n'+
        "space-delimited format (delimiters can be changed in the code)"+'\n'+'\n'+
        "Step 2: enter the column number related to the first interactor ID in the PPI dataset"+'\n'+'\n'+
        "Step 3: enter the column number related to the second interactor ID in the PPI dataset"+'\n'+'\n'+
        "Step 4: enter the file name containing the list of the seed genes, it must be a single column"+'\n'+'\n'+
        "Step 5: a report named 'user-input seed gene list name'+'interactions_results.txt' is generated" +'\n'+'\n'+
        "* * * * * * *" +'\n'+'\n'
     )
        

### end print instructions

###
      
### reading inputs

# enter *** reference interactome *** filename and then the *** columns to be read (1°, 2°, etc) ***

file_to_read_from = input("Enter reference interactome filename: ")

c1 = int(input("Enter interactor A column to read (1,2,3...): "))

c1=c1-1 # this because python starts counting form 0, not 1

c2 = int(input("Enter interactor B column to read (1,2,3...): "))

c2=c2-1

# enter *** seed list *** filename:

read_list = input("Enter seed list filename: ")

# calculating elapsed computing time

start_time = time.time()

###

### reading datasets and computation

list_to_read = open(read_list, 'r') # list of seed nodes

seed_list = list_to_read.readlines() # uploads the list in memory line by line

# strips away newlines: 

converted_seed_list = []

for element in seed_list:
    converted_seed_list.append(element.strip())

### initializing as many data lists as the columns you want (not all):

col1, col2, seedfound, interactorsfound = [],[],[],[]

### read given columns with given delimiter in file and memorize 
      
### WARNING ------- ALWAYS CHECK THE DELIMITER ---------- WARNING ###

with open(file_to_read_from, 'r') as file_in:
    reader = csv.reader(file_in, delimiter=' ') # can as well be ',' or '\t' (tab) or ';' or '\s' or ' ' (space) etc
    for row in reader:
        col1.append(row[c1]) # assuming col 1 in the file is one of the 2 you want
        col2.append(row[c2]) # assuming col 2 in the file is one of the 2 you want

### save stdout to file:

orig_stdout = sys.stdout
sys.stdout = open(read_list+'_interactions_results.txt', 'w')

print("***** FILE START *****")
print("")
print("Interaction dataset: " + file_to_read_from)
print("")
print("Seed genes dataset: " + read_list)
print("")

### search for seed genes in the two columns, count and write them out

number_of_seed_genes = str(len(converted_seed_list))
print('\n' + "#########################" +'\n')
print('\n'+"** List of original " + number_of_seed_genes + " SEED GENES"+'\n')
print(converted_seed_list)


print('\n'+"** List of SEED GENES found in the interaction dataset " + file_to_read_from + "(counter - gene name)" + '\n')

counter_seed = 0

for x in range(len(col1)):
    if (col1[x] in converted_seed_list):
        if (col1[x] not in seedfound):
            counter_seed = counter_seed + 1
            seedfound.append(col1[x])
            print (counter_seed,col1[x])
        else:
            pass
    else:
        pass

for x in range(len(col2)):
    if (col2[x] in converted_seed_list):
        if (col2[x] not in seedfound):
            counter_seed = counter_seed + 1
            seedfound.append(col2[x])
            print (counter_seed,col2[x])
        else:
            pass
    else:
        pass

number_seed_found = str(counter_seed)

print('\n'+ "** No." + number_seed_found + " SEED GENES found in " + file_to_read_from + " out of " + number_of_seed_genes + " original seed genes" + '\n')

### search if there are interactions *** among and only among nodes in the list *** and print them

print('\n' + "#########################" +'\n')
print('\n'+"** List of Interactions among SEED GENES THEMSELVES only " + "(counter - line in file - gene A - gene B)" + '\n') 

counter=0  # line counter (number of interactions detected)

# check if col1 entry and col2 entry are into list, print on screen and write on file

for x in range(len(col1)):
    if (col1[x] in converted_seed_list and col2[x] in converted_seed_list):
        counter=counter+1
        print (counter,x,col1[x],col2[x])
        # new_interactome.write(str(counter)+' '+str(x)+' ' +str(col1[x])+' '+str(col2[x])+'\n')
    else:
        pass


### searches and counts interactors of the seed genes:

print('\n' + "#########################" +'\n')
print('\n'+"** List of INTERACTORS (non seed genes) found in the dataset " + "(counter - gene name)" + '\n')

counter_interactors = 0

for x in range(len(col1)):
    if (col1[x] in converted_seed_list and col2[x] not in interactorsfound and col2[x] not in converted_seed_list):
        counter_interactors = counter_interactors + 1
        interactorsfound.append(col2[x])
        print (counter_interactors,col2[x])
    else:
        pass

for x in range(len(col2)):
    if (col2[x] in converted_seed_list and col1[x] not in interactorsfound and col1[x] not in converted_seed_list):
        counter_interactors = counter_interactors + 1
        interactorsfound.append(col1[x])
        print (counter_interactors,col1[x])
    else:
        pass

print('\n' + "Interactors found in dataset: " + str(counter_interactors) + '\n')




### search interactions among seed genes and interactors in the database and print them
print('\n' + "#########################" +'\n')
print('\n'+"** List of interactions among SEED GENES and THEIR DIRECT INTERACTORS " + "(counter - line in file - gene A - gene B)"+ '\n')

counter_interactions = 0  # line counter (number of interactions detected)

# check if col1 entry or col2 entry are into list, print on screen and write on file

for x in range(len(col1)):
    if (col1[x] in converted_seed_list or col2[x] in converted_seed_list):
        counter_interactions = counter_interactions+1
        print (counter_interactions, x, col1[x], col2[x])
        # new_interactome.write(str(counter_interactions)+' '+str(x)+' ' +str(col1[x])+' '+str(col2[x])+'\n')
    else:
        pass



### search all interactions seed genes-interactors and interactors-interactors and print them

print('\n' + "#########################" +'\n')
print('\n'+"** List of interactions among INTERACTORS only " + "(counter - line in file - gene A - gene B)"+ '\n') 

counter_nonseeds = 0  # line counter (number of interactions detected)

# check if col1 entry and col2 entry are into converted_seed_list, print on screen and write on file

for x in range(len(col1)):
    if (col1[x] in interactorsfound and col2[x] in interactorsfound):
        counter_nonseeds = counter_nonseeds + 1
        print (counter_nonseeds, x, col1[x], col2[x])
        # new_interactome.write(str(counter)+' '+str(x)+' ' +str(col1[x])+' '+str(col2[x])+'\n')
    else:
        pass

elapsed_time = time.time() - start_time
    
print('\n' + "#########################" +'\n')
print("")
print("* * * * * * *" +'\n')
print("SUMMARY" + '\n')
print("* * * * * * *" +'\n')

print('\n' + "Uploaded interaction dataset file: " + file_to_read_from)

print('\n' + "Uploaded seed genes dataset file: " + read_list)

print('\n'+ "SEED GENES found in interaction dataset: "+ number_seed_found + " out of " + number_of_seed_genes + " original seed genes")

print('\n'+"INTERACTORS of seed genes found in interaction dataset: " + str(counter_interactors))

print('\n'+"INTERACTIONS involving SEED GENES only: " + str(counter))

print('\n'+"INTERACTIONS involving SEED GENES and THEIR INTERACTORS: " + str(counter_interactions))

print('\n'+"INTERACTIONS involving INTERACTORS only: " + str(counter_nonseeds))

print('\n' + "Computed on", datetime.datetime.now(), "from seed dataset", read_list, "and interaction dataset", file_to_read_from)

print('\n' + "Elapsed computing time: " + str(elapsed_time) + " seconds" + '\n')

print("* * * * * * *" +'\n')

print("***** END OF FILE *****")


# new_interactome.close() # close the file

sys.stdout.close()

sys.stdout = orig_stdout



print('\n' + "########################################################")

print('\n' + "Results have been saved in file " + read_list +"_interactions_results.txt")

print('\n' + "Uploaded interaction dataset file: " + file_to_read_from)

print('\n' + "Uploaded seed genes dataset file: " + read_list)

print('\n'+ "SEED GENES found in interaction dataset: "+ number_seed_found + " out of " + number_of_seed_genes + " original seed genes")

print('\n'+"INTERACTORS of seed genes found in interaction dataset: " + str(counter_interactors))

print('\n'+"INTERACTIONS involving SEED GENES only: " + str(counter))

print('\n'+"INTERACTIONS involving SEED GENES and THEIR INTERACTORS: " + str(counter_interactions))

print('\n'+"INTERACTIONS involving INTERACTORS only: " + str(counter_nonseeds))

print('\n' + "Computed on", datetime.datetime.now(), "from seed dataset", read_list, "and interaction dataset", file_to_read_from)

print('\n' + "Elapsed computing time: " + str(elapsed_time) + " seconds" + '\n')


