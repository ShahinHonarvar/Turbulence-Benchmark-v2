def return_nth_smallest_ascii(s):
    if len(s) < 12:
        return None
    chunk = s[12:73]
    ascii_values = [ord(char) for char in chunk]
    ascii_values.sort()
    return chr(ascii_values[12 - 1])