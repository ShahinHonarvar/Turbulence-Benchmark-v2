def return_nth_smallest_ascii(s):
    ascii_values = sorted(map(ord, s[0:15]))
    nth_smallest = ascii_values[14]
    return chr(nth_smallest)