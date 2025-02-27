def return_nth_smallest_ascii(s):
    sub_string = s[17:84]
    ascii_values = [ord(c) for c in sub_string]
    sorted_values = sorted(ascii_values)
    return chr(sorted_values[4])