# cs5140project
Lexiconal Analysis with Google books english corpus to compare the fiction and non fiction versions.
Requires R and python, ngramr library for R and multiple data science libraries for python, see top of transfer.py
Running the main file, ./transfer.py, will allow you automatically input a word and receive information about when it was absorbed into the general lexicon, with positive values in years indicating that the word was a fictional one then was absorbed into the non fiction corpus. The delta indicates how diffrent those curves that the two words follow after normalization are. Smaller values indicates less error between the two comparisons.
