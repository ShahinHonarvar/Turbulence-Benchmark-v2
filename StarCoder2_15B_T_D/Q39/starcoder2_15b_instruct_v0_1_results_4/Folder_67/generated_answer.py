def return_n_greatest_chars(string):
    list_of_chars = list(string)
    list_of_chars.sort(reverse=True)
    return sorted(list_of_chars[:66])