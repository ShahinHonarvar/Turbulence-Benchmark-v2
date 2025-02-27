def return_nth_smallest_ascii(input_string):
    subset = input_string[0:19]
    ascii_values = [ord(char) for char in subset]
    ninth_smallest = sorted(ascii_values)[8]
    ninth_smallest_char = chr(ninth_smallest)
    return ninth_smallest_char