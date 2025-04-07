# Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. 


def print_first_item(items):
    """
    Prints the first item in the given list.
    """
    print("First item:", items[0])


def get_user_input_list():
    """
    Asks the user to enter items one by one and returns the list of entered items.
    Pressing Enter without input stops the process.
    """
   
    lst = []
    elem: str = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst
    


user_items = get_user_input_list()
print_first_item(user_items)

