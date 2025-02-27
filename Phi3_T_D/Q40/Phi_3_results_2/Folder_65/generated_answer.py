def return_n_smallest_chars(input_string):
    smallest_chars = sorted([char for char in input_string], key=ord)[:27]
    smallest_chars.reverse()
    return smallest_chars