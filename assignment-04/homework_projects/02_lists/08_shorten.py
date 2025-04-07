# Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. 




MAX_LENGTH = 3 

def shorten(lst):
    """
    Removes elements from the end of lst until its length is MAX_LENGTH.
    Prints each removed element. If lst is already within the limit, it remains unchanged.
    """
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop() 
        print("Removed:", removed_item)



def get_lst():
    """
    Prompts the user to enter elements one by one and returns the resulting list.
    """
    lst = []
    elem = input("Enter an element (or press Enter to finish): ")
    while elem:
        lst.append(elem)
        elem = input("Enter an element (or press Enter to finish): ")
    return lst

lst = get_lst()
shorten(lst)
print("Final list:", lst)


