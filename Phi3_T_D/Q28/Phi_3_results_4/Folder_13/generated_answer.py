def return_nth_smallest_ascii(input_string):
    subset_of_string = input_string[47:81]
    char_ascii_values = sorted([ord(char) for char in subset_of_string])
    return chr(char_ascii_values[3])