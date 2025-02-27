def return_nth_smallest_ascii(s):
    substring = s[0:14]
    ascii_values = sorted((ord(char) for char in substring))
    return chr(ascii_values[13])