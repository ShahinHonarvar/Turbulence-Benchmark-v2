def return_nth_smallest_ascii(s):
    start, end = (46, 82)
    nth_smallest = sorted(set(s[start:end + 1]), key=ord)[15]
    return nth_smallest