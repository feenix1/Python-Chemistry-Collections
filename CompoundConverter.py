import os
import periodictable as pt
import pyparsing

# Clear terminal function
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

# convert: Converts between units
# compound - string
# unit_from - g, mol, molecules
# unit_to - g, mol, molecules

def string_is_float(string):
  try:
    float(string)
    return True
  except ValueError:
    return False

def convert():
  while True:
    clear()
    compound = input("Enter the molecular compound formula [Ex: NaCl, C6 H12 O6, Na(SO)4]: ")
    if compound == "exit":
      return None
    formula = string_to_formula(compound)
    if formula == None:
      print("\nInvalid compound formula! Please try again.")
      input("Press enter to continue...")
      continue
    
    print("") # -----------------
    
    unit_from = input("Enter the unit to convert from [g, mol, molecules]: ")
    if unit_from == "exit":
      return None
    if not unit_from in ["g", "mol", "molecules"]:
      print("\nInvalid unit_from! Please try again.")
      input("Press enter to continue...")
      continue
    unit_from_amount = input(f"|---- Amount of {unit_from} to convert from: ")
    if unit_from_amount == "exit":
      return None
    if not string_is_float(unit_from_amount):
      print("\nInvalid unit_from_amount! Please try again.")
      input("Press enter to continue...")
      continue
    
    print("") # -----------------
    
    unit_to = input("Enter the unit to convert to [g, mol, molecules]: ")
    if unit_to == "exit":
      return None
    if not unit_to in ["g", "mol", "molecules"]:
      print("\nInvalid unit_to! Please try again.")
      input("Press enter to continue...")
      continue
    
    print("") # -----------------
    
    # Convert from mol
    if unit_from == "mol":
    # g
      if unit_to == "g":
        print(f"{unit_from_amount} mol of {compound} is \n  {float(unit_from_amount) * formula.mass} g")
        input("\nPress enter to continue...")
        return None
    # molec
      if unit_to == "molecules":
        print(f"{unit_from_amount} mol of {compound} is \n  {float(unit_from_amount) * formula.mass / formula.mass * 6.022e23} molecules")
        input("\nPress enter to continue...")
        return None
    # Convert from g
    if unit_from == "g":
    # mol
      if unit_to == "mol":
        print(f"{unit_from_amount} g of {compound} is \n  {float(unit_from_amount) / formula.mass} mol")
        input("\nPress enter to continue...")
        return None
    # molec
      if unit_to == "molecules":
        print(f"{unit_from_amount} g of {compound} is \n  {float(unit_from_amount) / formula.mass * 6.022e23} molecules")
        input("\nPress enter to continue...")
        return None
    # Convert from molec
    if unit_from == "molecules":
      # g
      if unit_to == "g":
        print(f"{unit_from_amount} molecules of {compound} is \n  {float(unit_from_amount) * formula.mass / 6.022e23} g")
        input("\nPress enter to continue...")
        return None  
      # mol
      if unit_to == "mol":
        print(f"{unit_from_amount} molecules of {compound} is \n  {float(unit_from_amount) * formula.mass / 6.022e23 / formula.mass} mol")
        input("\nPress enter to continue...")
        return None
    
    else:
      print("\nInvalid unit_to! Please try again.")
      input("Press enter to continue...")
      continue
  
# mass: displays the mass of a compound in g/mol
# compound - string

def mass():
  compoundInput = input("Enter the molecular compound formula [Ex: NaCl, C6 H12 O6, Na(SO)4]: ")
  if compoundInput == "exit":
    return None
  
  formula = string_to_formula(compoundInput)
  if formula == None:
    print("Invalid compound formula! Please try again.\n")
    input("Press enter to continue...")
    return None
  
  print(f"The Molar Mass of {compoundInput} is: {formula.mass} g/mol\n")
  input("Press enter to continue...")

while (True):
  clear()
  print("Compound Converter - By Matthew Dinh")
  print("Type exit at any point to exit the command or program.\n")
  
  command = input("Enter a command [Ex: help, exit]: ")
  if command == "help":
    print("")
    print("help - Displays this help message")
    print("convert - Requires a compound, unit_from, and unit_to - Converts between units.")
    print("mass - Requires a compound - Displays the mass of a compound in g/mol")
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
    


    
    