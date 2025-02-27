def return_nth_smallest_ascii(s):
    substring = s[3:27]
    sorted_chars = sorted(substring)
    return sorted_chars[4]