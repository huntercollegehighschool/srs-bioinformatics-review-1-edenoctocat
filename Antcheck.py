"""
Define a function isDNA that takes a single string as an input. The string is supposed to represent a DNA string that only has molecules A, C, G, and T. The function returns True(the Boolean value) if the string is a valid DNA string, and False if it's not.
"""

def isDNA(dna):
  for nt in dna:
    if not (nt == "A" or nt == "C" or nt == "G" or nt == "T"):
      return False
  return True