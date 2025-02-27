def return_nth_smallest_ascii(s):
    substr = s[67:78]
    sorted_chars = sorted(set(substr))
    return sorted_chars[6]