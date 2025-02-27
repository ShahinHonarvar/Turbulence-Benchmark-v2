def return_n_smallest_chars(input_string):
    smallest_chars = [character for character in input_string if ord(character) <= 66]
    smallest_chars.sort(reverse=True)
    return smallest_chars[:66]