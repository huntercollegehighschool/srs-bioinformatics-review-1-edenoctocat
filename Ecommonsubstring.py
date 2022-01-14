"""
Define a function commonsubstring that takes a list of DNA strings as an input.

-First the function should check if all strings in the list are valid DNA strands (use the function defined in the 1st part). If it's not, return "error".

-If all strings in the list are valid, the function then finds the longest nucleotide substring that is in all of the strings in the list and returns it as a list. If multiples such strings exist, the function should include them all in the returned list.

For example,
commonsubstring("ACGCT", "CGCCA", "ATTACGCT") should return ["CGC"]
"""
from Antcheck import isDNA

def commonsubstring(dnalist):
  i = 0
  while isDNA(dnalist[i]):
    i += 1
    if i == len(dnalist):
      break
  else: return "error"
  dna1 = min(dnalist, key = len)
  dnalist.remove(dna1)
  substrings = []
  for x in range(len(dna1)+1):
    for y in range(len(dna1)+1):
      if y > x:
        if dna1[x:y] in dnalist[0]:
          substrings.append(dna1[x:y])
  for dna in dnalist[1:]:
    for string in substrings:
      print(string)
      if string not in dna:
        substrings.remove(string)
  commonsub = []
  for string in substrings:
    if len(string) == len(max(substrings, key = len)):
      commonsub.append(string)
  return commonsub