def return_nth_smallest_ascii(s):
    ascii_values = [ord(char) for i, char in enumerate(s) if 0 <= i <= 69]
    ascii_values.sort()
    return chr(ascii_values[9]) if len(ascii_values) >= 10 else None