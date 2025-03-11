def new_list():
    newlist = {
        "first": None,
        "last": None,
        "size": 0,
    }
    return newlist

def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]
        
def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]
    count = 0
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1
            
    if not is_in_array:
        count = -1
    return count

def add_first(my_list, element):
    #Agrega un elemento al inicio de la lista.
    #Agrega un nuevo nodo al inicio de la lista y aumenta el tamaño de la lista en 1.
    #En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.
    new_node = {'info': element, 'next': my_list['first']}
    
    if my_list['size'] == 0:
        my_list['last'] = new_node
    
    my_list['first'] = new_node
    my_list['size'] += 1
    
    return my_list

def add_last(my_list, element):
    #Agrega un elemento al final de la lista.
    #Agrega un nuevo nodo al final de la lista y aumenta el tamaño de la lista en 1.
    #En caso de que la lista esté vacía, el primer y último nodo de la lista serán el nuevo nodo.
    new_node = {'info': element, 'next': None}
    
    if my_list['size'] == 0:
        my_list['first'] = new_node
    else:
        my_list['last']['next'] = new_node
    
    my_list['last'] = new_node
    my_list['size'] += 1
    
    return my_list

def size(my_list):
    #Retorna el tamaño de la lista.
     return my_list['size']
 
def firs_element(my_list):
    #Retorna el primer elemento de una lista no vacía.
    #Retorna el primer elemento de la lista. Si la lista está vacía, lanza un error IndexError: list index out of range. 
    # Esta función no elimina el elemento de la lista.
    
    if my_list['size'] == 0:
        raise Exception('IndexError: list index out of range')
    return my_list['first']['info']

def sub_list(my_list, pos_i, num_elements):
    """
    Retorna una sublista desde la posición `pos_i` con `num_elements` elementos.
    """
    if my_list["size"] == 0 or pos_i < 1 or pos_i > my_list["size"]:
        raise IndexError("Posición fuera de rango.")

    new_sublist = new_list()  
    current = my_list["first"]
    index = 1

    while current is not None and num_elements > 0:
        if index >= pos_i:
            add_last(new_sublist, current["info"])
            num_elements -= 1
        current = current["next"]
        index += 1

    return new_sublist

def iterator(lst):
   
    return [element for element in lst]


def selection_sort(my_list, sort_crit):
    
    if my_list["size"] < 2:
        return my_list  

    current = my_list["first"]

    while current is not None:
        min_node = current
        next_node = current["next"]

        while next_node is not None:
            if sort_crit(next_node["info"], min_node["info"]):
                min_node = next_node
            next_node = next_node["next"]

        current["info"], min_node["info"] = min_node["info"], current["info"]

        current = current["next"]

    return my_list


def insertion_sort(my_list, sort_crit):
    
    if my_list["size"] < 2:
        return my_list  

    sorted_list = {"size": 0, "first": None}

    current = my_list["first"]

    while current is not None:
        new_node = {"info": current["info"], "next": None}

        if sorted_list["first"] is None or sort_crit(new_node["info"], sorted_list["first"]["info"]):
            new_node["next"] = sorted_list["first"]
            sorted_list["first"] = new_node
        else:
            prev = sorted_list["first"]
            while prev["next"] is not None and not sort_crit(new_node["info"], prev["next"]["info"]):
                prev = prev["next"]

            new_node["next"] = prev["next"]
            prev["next"] = new_node

        sorted_list["size"] += 1
        current = current["next"]

    return sorted_list


