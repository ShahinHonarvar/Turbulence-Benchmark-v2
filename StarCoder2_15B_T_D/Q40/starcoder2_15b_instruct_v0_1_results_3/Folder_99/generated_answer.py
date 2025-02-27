def return_n_smallest_chars(string):
    ascii_values = [ord(c) for c in string]
    ascii_values.sort()
    return [chr(value) for value in ascii_values[:35]]