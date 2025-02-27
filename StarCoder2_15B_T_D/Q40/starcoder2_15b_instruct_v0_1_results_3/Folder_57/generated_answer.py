def return_n_smallest_chars(string):
    ascii_values = [ord(char) for char in string]
    sorted_values = sorted(ascii_values, reverse=True)
    return [chr(value) for value in sorted_values[:29]]