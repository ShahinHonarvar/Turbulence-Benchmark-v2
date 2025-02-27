def return_n_smallest_chars(string):
    list_of_chars = sorted(list(set(string)), key=ord)
    return list_of_chars[:66][::-1]