tors interactor finder

tors_interactor_finder is a small, simple and stupid Python 3 app to search interactions starting from a seed list and an interaction dataset.

Its original use is intended in network biology and network medicine, but of course it can be used to dig into any type of interaction dataset. You don't need any programming skill to use tors (neither do I :-).

Starting from your seed genes list, tors searches for their interactors and related interactions, and generates a report with interaction data to be used for further network analysis.

What you need is 1) a Python 3 installation, 2) a file containing your starting seeds (genes, or any other type of 'node'), and 3) an interaction dataset file, representing your network in Simple Interaction Format (SIF), i.e. nothing else represented as (at least) two columns, one for each interactor, as for example:

A (interacting with) B

A C

A D

B D

C A

C B

...

It can easily be used by typing on the terminal the following instructions:

python tors_interaction_finder_p3_ok.py

and following the few further instructions on screen. 

Example interaction dataset, seed genes and result files are provided.

Here below follows a typical stdout.

################

prompt:$ python tors_interactor_finder_p3_ok.py

###########################################################################################

TORS SEARCHES FOR BINARY INTERACTIONS IN PPI DATASETS STARTING FROM A LIST OF SEED GENES
###########################################################################################

* * * * * * *

Instructions:

Step 1: enter the file name of the PPI dataset containing all interaction pairs,
the dataset must be at least two columns (interactor A - interactor B) and
space-delimited format (delimiters can be changed in the code)

Step 2: enter the column number related to the first interactor ID in the PPI dataset

Step 3: enter the column number related to the second interactor ID in the PPI dataset

Step 4: enter the file name containing the list of the seed genes, it must be a single column

Step 5: a report named 'user-input seed gene list name'+'interactions_results.txt' is generated

* * * * * * *


Enter reference interactome filename: interaction_dataset.txt
Enter interactor A column to read (1,2,3...): 1
Enter interactor B column to read (1,2,3...): 2
Enter seed list filename: seed_genes_list.txt

########################################################

Results have been saved in file seed_genes_list.txt_interactions_results.txt

Uploaded interaction dataset file: interaction_dataset.txt

Uploaded seed genes dataset file: seed_genes_list.txt

SEED GENES found in interaction dataset: 87 out of 224 original seed genes

INTERACTORS of seed genes found in interaction dataset: 123

INTERACTIONS involving SEED GENES only: 10

INTERACTIONS involving SEED GENES and THEIR INTERACTORS: 146

INTERACTIONS involving INTERACTORS only: 15

Computed on 2021-05-04 17:43:52.901537 from seed dataset seed_genes_list.txt and interaction dataset interaction_dataset.txt

Elapsed computing time: 0.08770513534545898 seconds

################

