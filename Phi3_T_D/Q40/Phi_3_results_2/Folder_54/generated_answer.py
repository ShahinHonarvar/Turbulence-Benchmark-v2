def return_n_smallest_chars(input_string):
    characters = sorted([char for char in input_string])
    smallest_chars = characters[:79]
    smallest_chars.sort(reverse=True)
    return smallest_chars