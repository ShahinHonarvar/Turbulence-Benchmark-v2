def return_nth_smallest_ascii(s):
    chars = s[:10]
    sorted_chars = sorted(chars)
    return sorted_chars[9]