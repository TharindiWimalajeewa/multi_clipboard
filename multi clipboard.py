#store multiple things in clip board 

import sys
import clipboard
import json

SAVED_DATA = "clipboard.json"

def save_items(filepath, data): #here the data is like a python dictonary
    with open(filepath,"w") as f:
        json.dump(data,f)

def load_items(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

save_items("test.json", {"key":"value"})

if len(sys.argv) ==2:
    command = sys.argv[1] 
    data = load_items(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_items(SAVED_DATA, data)
        print("data saved")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("data loaded")
        else: print("key doesn't exist")
      
    elif command == "list":
        print(data)
    else: print("unknown command")


else: print("please pass exactly one command")