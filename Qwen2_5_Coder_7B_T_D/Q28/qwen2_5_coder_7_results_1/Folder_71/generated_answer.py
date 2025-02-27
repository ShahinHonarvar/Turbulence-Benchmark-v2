def return_nth_smallest_ascii(s):
    sliced = s[5:83]
    sorted_chars = sorted(sliced)
    return sorted_chars[15]