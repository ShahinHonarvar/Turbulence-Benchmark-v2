def return_nth_smallest_ascii(s):
    ascii_values = [ord(c) for c in s[51:90]]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[13])