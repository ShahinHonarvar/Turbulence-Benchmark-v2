def return_n_smallest_chars(string):
    sorted_string = sorted(string)
    reversed_string = reversed(sorted_string)
    sliced_string = list(reversed_string)[:45]
    return sliced_string