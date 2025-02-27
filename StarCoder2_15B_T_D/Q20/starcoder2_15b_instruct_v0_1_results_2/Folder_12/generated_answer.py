def find_n_th_smallest_num(input_list):
    """
    This function takes a list of distinct numbers as input and returns the 14th smallest number from index 40 to index 68, both inclusive.
    """
    sorted_list = sorted(input_list[40:70])
    return sorted_list[13]