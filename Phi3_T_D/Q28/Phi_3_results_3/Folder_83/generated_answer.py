from itertools import islice

def return_nth_smallest_ascii(s):
    selected_chars = islice(s, 30, 71)
    ascii_values = [ord(char) for char in selected_chars]
    ascii_values.sort()
    fifteenth_smallest_ascii = ascii_values[14]
    char = chr(fifteenth_smallest_ascii)
    return char