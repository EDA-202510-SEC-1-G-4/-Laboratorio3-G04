def new_list():
    newlist = {
        "elements": [],
        "size": 0
    
    }
    return newlist

def add_first(list, element):
    list['elements'].insert(0, element)
    list['size'] += 1
    return list

def add_last(list, element):
    list['elements'].append(element)
    list['size'] += 1
    return list

def size(list):
    return list['size']

def first_element(list):
    if list['size'] != 0:
        return list['elements'][0]

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
    return -1
    