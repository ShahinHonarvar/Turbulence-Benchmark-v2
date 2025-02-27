def return_nth_smallest_ascii(input_string):
    characters = input_string[0:5]
    ascii_values = [ord(c) for c in characters]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[3])