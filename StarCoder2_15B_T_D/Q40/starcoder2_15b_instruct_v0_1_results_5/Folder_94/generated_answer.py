def return_n_smallest_chars(string):
    list_of_chars = list(string)
    sorted_list = sorted(list_of_chars, key=ord)
    return sorted_list[-87:]