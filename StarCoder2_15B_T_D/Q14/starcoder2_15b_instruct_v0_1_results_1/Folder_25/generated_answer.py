from index 37 to index 76, both inclusive. If there is no such an element, it returns None.

def find_second_smallest_num(input_list):
    """
    This function takes a list of distinct numbers as input and returns the second smallest element
    """
    sorted_list = sorted(input_list)
    if len(sorted_list) >= 38:
        return sorted_list[37]
    else:
        return None