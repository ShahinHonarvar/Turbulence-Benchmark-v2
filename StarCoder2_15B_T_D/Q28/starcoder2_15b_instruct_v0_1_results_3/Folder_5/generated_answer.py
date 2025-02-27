def return_nth_smallest_ascii(string):
    chars = list(string)
    sorted_chars = sorted(chars, key=lambda c: ord(c))
    sliced_chars = sorted_chars[5:90]
    return sliced_chars[12]