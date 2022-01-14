"""
Define a function reversecomplement that takes a DNA string as an input. 

-First the function should check if it is a valid DNA strand (use the function defined in the 1st part). If it's not, return "error".

-If it is a valid DNA string, the function finds the reverse complement of that string. The reverse complement is found by first reversing the string, then taking the complement of each nucleotide. A and T are complements of each other, and C and G are complements of each other.

For example,
reversecomplement("AAGCT") should return "AGCTT".
"""
from Antcheck import isDNA

def reversecomplement(dna):
  if isDNA(dna) == False:
    return "error"
  else:
    reverse = dna[::-1]
    revcompl = ""
    for nt in reverse:
      if nt == "A":
        revcompl += "T"
      elif nt == "T":
        revcompl += "A"
      elif nt == "C":
        revcompl += "G"
      elif nt == "G":
        revcompl += "C"
    return revcompl
    