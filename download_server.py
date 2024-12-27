#!/usr/bin/env python3

from serverlib import *

def print_help():
    print(f"usage: {sys.argv[0]} [vanilla|paper|forge|fabric] [path] [version]")

def main():
    class_dictionary = {
        "vanilla": Vanilla,
#        "paper": Paper,
#        "forge": Forge,
#        "fabric": Fabric
    }
    
    if (os.name == 'nt'):
        print("This script is not compatible with Windows. Please download a real OS before continuing.")
        return 1
    try:
     class_dictionary[sys.argv[1].lower()].create_server(sys.argv[2],sys.argv[3])
    except:
     print_help()

if __name__ == "__main__":
    main()
