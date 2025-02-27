def return_nth_smallest_ascii(string):
    characters = list(string[0:5])
    ascii_values = [ord(c) for c in characters]
    sorted_ascii_values = sorted(ascii_values)
    return chr(sorted_ascii_values[3])