def return_nth_smallest_ascii(string):
    chars = [c for c in string if 25 <= string.index(c) <= 77]
    sorted_chars = sorted(chars)
    return sorted_chars[15]