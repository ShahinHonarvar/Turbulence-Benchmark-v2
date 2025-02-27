def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    reversed_string = sorted_string[::-1]
    return list(reversed_string[:59])