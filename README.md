tors interactor finder

tors_interactor_finder is a small, simple and stupid Python 3 app to search interactions starting from a seed list and an interaction dataset.

Its original use is intended in network biology and network medicine, but of course it can be used to dig into any type of interaction dataset. You don't need any programming skill to use tors.

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

