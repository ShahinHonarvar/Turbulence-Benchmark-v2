def find_second_smallest_num(input_list):
    """
    Write a function called 'find_second_smallest_num' that takes one argument, a list of distinct numbers, as input and returns the second smallest element from index 10 to index 66, both inclusive. If there is no such an element, the function should return 'None'.
    """
    sorted_list = sorted(input_list)
    if len(sorted_list) < 67:
        return None
    return sorted_list[10:67][1]