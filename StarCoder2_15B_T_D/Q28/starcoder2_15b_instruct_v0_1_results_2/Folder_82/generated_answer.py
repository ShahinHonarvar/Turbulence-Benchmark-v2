def return_nth_smallest_ascii(string):
    chars = list(string)
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    return sorted_chars[14]