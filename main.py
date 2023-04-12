import os
import pyparsing
import periodictable as pt

def Clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def StringToFormula(stringCompound):
  if stringCompound == "":
    return None
  try:
    compound = pt.formula(stringCompound)
    return compound
  except pyparsing.exceptions.ParseException or ValueError:
    return None

while True:
  Clear()
  print("Welcome to Python Chemistry Collections!")
  print("This program is a collection of chemistry tools written in Python by Matthew Dinh.")
  print("Type 'exit' to exit the program at any time.")
  print("")
  print("1 [Compound Converter]")
  print("2 [BCA Complete]")
  print("")
  toolIndex = input("Please select a tool to use: ")
  if toolIndex == "exit":
    break
  if toolIndex.isnumeric() == False:
    print("Invalid tool! Please try again.")
    input("Press enter to continue...")
    continue
  
  toolIndex = int(toolIndex)
  if toolIndex == 1:
    exec(open("CompoundConverter.py", "r").read())
  if toolIndex == 2:
    exec(open("BCAComplete.py", "r").read())
