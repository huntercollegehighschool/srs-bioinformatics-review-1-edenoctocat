"""
Define a function ntcount that takes a string representing a DNA string. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA strand, the function returns a dictionary with the counts of each nucleotide.

For example: 
ntcount("AACTGTA") 
returns {"A": 3, "C": 1, "G": 1, "T": 2}
"""
from Antcheck import isDNA

def ntcount(dna):
  if isDNA(dna) == False:
    return "error"
  else:
    count = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nt in dna:
      count[nt] += 1
    return count