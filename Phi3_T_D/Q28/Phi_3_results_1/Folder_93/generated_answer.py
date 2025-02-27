def return_nth_smallest_ascii(s):
    start, end = (42, 59)
    return sorted(s[start:end + 1])[16]