def return_nth_smallest_ascii(s):
    specific_chars = s[0:5]
    nth_smallest_ascii = sorted(specific_chars)[:4][-1]
    return nth_smallest_ascii