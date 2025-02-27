def return_nth_smallest_ascii(text):
    ascii_values = sorted(set((ord(char) for char in text[18:67])))
    return chr(ascii_values[18])