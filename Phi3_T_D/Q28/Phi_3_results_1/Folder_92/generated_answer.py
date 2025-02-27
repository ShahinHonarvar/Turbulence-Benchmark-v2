def return_nth_smallest_ascii(s):
    ascii_values = sorted([ord(char) for char in s[0:4]])
    return chr(ascii_values[3])