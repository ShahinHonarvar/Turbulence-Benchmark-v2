def return_n_smallest_chars(string):
    chars = list(string)
    chars.sort()
    smallest_chars = chars[:37]
    smallest_chars.reverse()
    return smallest_chars