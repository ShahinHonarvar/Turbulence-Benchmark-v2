def return_nth_smallest_ascii(s):
    sub_string = s[17:84]
    sorted_chars = sorted(set(sub_string))
    return sorted_chars[4]