def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort(key=ord)
    return chars[:37][::-1]