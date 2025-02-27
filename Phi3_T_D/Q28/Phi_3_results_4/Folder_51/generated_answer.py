def return_nth_smallest_ascii(s):
    start, end = (10, 73)
    return min(s[start:end + 1], key=lambda c: ord(c))