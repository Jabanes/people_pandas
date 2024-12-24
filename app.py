import pandas as pd
from enum import Enum
import os
import platform

class Options(Enum):
    NAMES = 1
    AGES = 2
    IDS = 3
    STATUSES = 4
    EXIT = 5

def printMenu():
    for option in Options:
        print(f"{option.value} - {option.name}")

def searchItem(list_to_search, item_to_search, collumName):
   try:
        item_to_search = int(item_to_search)
        print(f"Searching {list_to_search[item_to_search]}...")
        count = df[df[collumName] == list_to_search[item_to_search]].shape[0] 
        print(f"Found: {count}")

        filtered = df[df[collumName] == list_to_search[item_to_search]]
        print(filtered)
        
   except ValueError:
      print("Invalid input")
   except IndexError:
      print("Out of range!")

def clear_terminal():

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  
df = pd.read_json('people_data.json')


if __name__ == "__main__":
    ids = list(df['id'].unique())
    names = list(df['name'].unique())
    ages = list(df['age'].unique())
    statuses = list(df['status'].unique())

    while True:
        printMenu()
        user_selection = input("select an option: ")
        clear_terminal()
        if user_selection.isdigit():

            user_selection = Options(int(user_selection))
            if user_selection == Options.NAMES:
                print("NAMES")
                print("-----------------------------------------")
                for index, i in enumerate(names):
                    print(f"{index}:  Name - {i}")

                nameToFind = (input("Select a name to find (by index): "))
                searchItem(names, nameToFind, 'name')

            elif user_selection == Options.AGES:
                    print("AGES")
                    print("-----------------------------------------")
                    for index, i in enumerate(ages):
                     print(f"{index}: Age - {i}")

                    ageToFind = (input("Select an Age to find (by index): "))
                    searchItem(ages, ageToFind, 'age')
            
            elif user_selection == Options.IDS:
                    print("ID's")
                    print("-----------------------------------------")
                    for index, i in enumerate(ids):
                     print(f"{index}: ID - {i}")

                    idToFind = (input("Select an ID to find (by index): "))
                    searchItem(ids, idToFind, 'id')

            elif user_selection == Options.STATUSES:
                    print("Statuses")
                    print("-----------------------------------------")
                    for index, i in enumerate(statuses):
                     print(f"{index}: Status - {i}")

                    statusToFind = (input("Select a status to find (by index): "))
                    searchItem(statuses, statusToFind, 'status')

            elif user_selection == Options.EXIT:
                    exit()
            
        else:
            print("Invalid")

