from itertools import islice

def return_nth_smallest_ascii(s):
    selected_chars = islice(s, 1, 37)
    sorted_chars = sorted(selected_chars, key=ord)
    return sorted_chars[14]