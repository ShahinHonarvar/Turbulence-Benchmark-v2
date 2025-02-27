def return_nth_smallest_ascii(char_string):
    slice = char_string[35:53]
    ascii_values = [ord(char) for char in slice]
    ascii_values.sort()
    return chr(ascii_values[9]) if len(ascii_values) > 9 else None