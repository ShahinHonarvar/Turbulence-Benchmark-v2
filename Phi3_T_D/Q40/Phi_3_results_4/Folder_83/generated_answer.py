def return_n_smallest_chars(input_string):
    smallest_chars = [(char, ord(char)) for char in input_string]
    smallest_chars.sort(key=lambda x: x[1])
    return [char for char, _ in smallest_chars[:38]]