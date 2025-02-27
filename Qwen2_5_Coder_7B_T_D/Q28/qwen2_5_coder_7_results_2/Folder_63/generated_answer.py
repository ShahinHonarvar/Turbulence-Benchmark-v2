def return_nth_smallest_ascii(s):
    sliced_str = s[47:71]
    sorted_chars = sorted((c for c in sliced_str))
    return sorted_chars[13]