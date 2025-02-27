def return_nth_smallest_ascii(input_string):
    ascii_values = {char: ord(char) for char in input_string[7:65] if char not in [' ', '\\    ', '']}
    return min(ascii_values, key=ascii_values.get) if len(ascii_values) >= 6 else None