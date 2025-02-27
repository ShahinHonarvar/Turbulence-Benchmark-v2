def return_nth_smallest_ascii(string):
    ascii_values = [ord(char) for char in string]
    sliced_values = ascii_values[51:61]
    sorted_values = sorted(sliced_values)
    return chr(sorted_values[4])