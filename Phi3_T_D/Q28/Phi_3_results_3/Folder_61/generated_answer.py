def return_nth_smallest_ascii(s):
    substring = s[0:10]
    ascii_values = sorted(substring)
    return ascii_values[9]