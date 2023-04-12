import os
import pyparsing
import periodictable as pt
import math

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

class BCATable:

# BCA Tables will be represented as a class with multiple lists

# A table will always have
# Reactants = [Compound, Compound, ...]
# Products = [Compound, Compound, ...]

# Each Reactant/Product will have a Before, Change, and After list
# compounds are from the periodictable library



