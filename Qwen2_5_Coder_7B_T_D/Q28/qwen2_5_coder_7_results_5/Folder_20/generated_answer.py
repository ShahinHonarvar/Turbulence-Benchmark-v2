def return_nth_smallest_ascii(s):
    return sorted([c for c in s if 25 <= ord(c) <= 64])[5]