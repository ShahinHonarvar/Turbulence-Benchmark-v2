def return_nth_smallest_ascii(s):
    sliced_chars = s[28:68]
    char_ascii_values = [ord(char) for char in sliced_chars]
    sorted_ascii_values = sorted(char_ascii_values)
    return chr(sorted_ascii_values[14])