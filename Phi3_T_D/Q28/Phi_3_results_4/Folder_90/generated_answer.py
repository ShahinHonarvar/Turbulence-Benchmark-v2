def return_nth_smallest_ascii(s):
    sub_string = s[17:84]
    unique_chars = sorted(set(sub_string))
    if len(unique_chars) < 5:
        return None
    return unique_chars[4]