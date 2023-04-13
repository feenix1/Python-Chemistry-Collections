import os
import pyparsing
import periodictable as pt
import math

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def parse_command(commandString):
  for char in commandString:
    if char == " ":
      return commandString.split(" ")
    else:
      return commandString

# class BCATable:

# BCA Tables will be represented as a class with multiple lists

# A table will always have
# Reactants = [Compound, Compound, ...]
# Products = [Compound, Compound, ...]

# Each Reactant/Product will have a Before, Change, and After list
# compounds are from the periodictable library

while (True):
  clear()
  print("BCA Complete - By Matthew Dinh")
  print("Type exit at any point to exit the command or program.\n")
  
  command = input("Enter a command [Ex: help, exit]: ")
  if command == "help":
    print("")
    print("help - Displays this help message")
    print("new - Creates a new BCA table, and deletes the current one")
    print("set compound - Requires a compound and a reaction/product index. Sets a reactant or product in the reaction.")
    print("set compound amount - Requires a  - Displays the mass of a compound in g/mol")
    print("view - Displays the current BCA table")
    
    print("exit - Exits the program")
    print("")
    input("Press enter to continue...")
  if command == "convert":
    print("")
    convert()
  if command == "mass":
    print("")
    mass()
  if command == "exit":
    break
