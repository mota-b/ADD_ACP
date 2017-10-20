import os
import get_key as gt
import numpy as np
import json
on = os.name

def print_menu(title, my_list, index):
    print("\n\t{0}\n".format(title))
    for e in my_list:
        i = my_list.index(e)
        
        if index == i:
            print("-{0}) {1} (!)".format(i, e["title"]))
        else:
            print("-{0}) {1}".format(i, e["title"]))


def menu(men):
    title = men["title"]
    my_list = men["list"]

    length = len(my_list)
    index = 0

    
    while True:
        os.system('cls' if on == 'nt' else 'clear')
        print_menu(title, my_list, index)
        key = gt.get()

        # Test key_board input
        if key == "up" or key == "left":
            index -= 1
                
        elif key == "down" or key == "right":
            index += 1 
        
        elif key == 127: break

        elif key == ord('q') or key == ord('Q'): return -1
        
        elif key == 13 :
            if men["list"][index]["isMen"] == True:
                if( menu(men["list"][index]) == -1 ):
                    break
            elif men["list"][index]["isMen"] == False:
                print("|")
                print("|")
                print("V\n")
                
                elem = men["list"][index]["list"][0]
                type_e = type(men["list"][index]["list"][0])
                if type_e == type("") :
                    print( np.array( json.loads( elem ) ) )
                else :
                    print(elem)
                k = gt.wait()
                if k == ord('q') or k == ord('Q'): return -1 
            


        # Watch interval menu
        if index >= length:
            index = 0
        else:
            if index < 0:
                index = (length-1)
        

