import os
import pyparsing
import periodictable as pt
import prettytable
import math

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def string_to_formula(stringCompound):
  if stringCompound == "":
    return None
  try:
    compound = pt.formula(stringCompound)
    return compound
  except pyparsing.exceptions.ParseException or ValueError:
    return None

def string_is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

def parse_command(commandString):
  for char in commandString:
    if char == " ":
      return commandString.split(" ")
    else:
      return commandString

class BCATable:
  # reaction[0] - reactants
  # reaction[1] - products
  _reaction = [[],[]]
    
  # table_view[0] reaction
  # table_view[1] before
  # table_view[2] change
  # table_view[3] after
  _table_view = [[],[],[],[]]
  
  def add_compound(compound, type):
    if string_to_formula(compound) == None:
      return "Invalid compound!"
    
    if type == "reactant":
      global _reaction
      _reaction[0].append(compound)
      return True
    elif type == "product":
      _reaction[1].append(compound)
      return True
    else:
      return "Invalid type!"
  
  def display():
    displaytable = prettytable(BCATable._table_view[0])
    displaytable.add_rows(BCATable._table_view[1:])
    print(displaytable)
    return None
    
  
# BCA Tables will be represented as a class with multiple lists

# A table will always have a reaction
# Reactants = [Compound, Compound, ...]
# Products = [Compound, Compound, ...]

# Each Reactant/Product will have a Before, Change, and After list
# compounds are from the periodictable library

bca_tables = []

while (True):
  clear()
  print("BCA Complete - By Matthew Dinh")
  print("Type exit at any point to exit the command or program.\n")
  
  commandString = input("Enter a command [Ex: help, exit]: ")
  command = parse_command(commandString)
  if command == ["help"]:
    print("")
    print("help - Displays this help message")
    print("new - Creates a new BCA table, and sets it as the current table")
    print("select [index] - Selects the table at the index, setting it as the current table.")
    print("duplicate [with_values] (index) - Duplicates the current table or the table at the index, and sets it as the current table.")
    print("delete [index] - Deletes the table at the index.")
    print("set [compound] [type] - Sets a reactant or product in the reaction of the current table.")
    print("solve [compound] [amount] [unit] - Fills out the rest of the BCA table with the calculated values based on the given compound.")
    print("view - Displays the current BCA table.")
    
    print("exit - Exits the program")
    print("")
    input("Press enter to continue...")
  if command == ["new"]:
    bca_tables.append(BCATable())    
  if command[0] == ["view"]:
    bca_tables[command[1]].display()
  if command == ["exit"]:
    break
