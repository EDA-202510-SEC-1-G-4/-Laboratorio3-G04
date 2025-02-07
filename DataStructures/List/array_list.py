def new_list1():
    newlist = {
        "elements": [],
        "size": 0
    
    }
    return newlist

def get_element(list, index):
    
        return list['elements'][index]
    
def is_present(my_list, element, compare_function):
    
    size = my_list['size']
    if size > 0:
        keyexists = False
        for keypos in range (0, size):
            info = my_list['elements'][keypos]
            if compare_function(element, info) == 0:
                keyexists = True
                break
        if keyexists:
            return keypos
    return element in list['elements']
    