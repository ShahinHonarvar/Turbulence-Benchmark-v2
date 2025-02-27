def return_nth_smallest_ascii(string):
    selected_characters = string[32:68]
    ascii_values = sorted(map(ord, selected_characters))
    return chr(ascii_values[11])