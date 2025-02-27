def return_nth_smallest_ascii(s):
    if len(s) < 11:
        return None
    sub_string = s[:11]
    sorted_chars = sorted(sub_string)
    return sorted_chars[10]