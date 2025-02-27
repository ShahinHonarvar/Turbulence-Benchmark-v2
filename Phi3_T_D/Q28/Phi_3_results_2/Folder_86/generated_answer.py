def return_nth_smallest_ascii(s):
    char_within_range = s[44:69 + 1]
    return sorted(char_within_range, key=ord)[14]