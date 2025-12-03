#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = my_list.copy()
    if idx < 0 or idx >= len(new_list):
        return new_list
    del new_list[idx]
    return new_list            
            
         
       
