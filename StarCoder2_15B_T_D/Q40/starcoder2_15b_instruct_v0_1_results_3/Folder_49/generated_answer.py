def return_n_smallest_chars(string):
    list_of_chars = sorted(string, key=ord)
    sorted_list = list_of_chars[:76][::-1]
    return sorted_list