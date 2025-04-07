# Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.


def print_last_item(items):
    """
    Prints the last item in the given list.
    """
    print("Last item:", items[-1])



def get_user_input_list():
    """
    Asks the user to enter items one by one and returns the list of entered items.
    Pressing Enter without input stops the process.
    """
    items = []
    
    while True:
        item = input("Enter an item (or press Enter to finish): ")
        if item == "":
            break 
        items.append(item)
    
    return items


user_items = get_user_input_list()
print_last_item(user_items)



