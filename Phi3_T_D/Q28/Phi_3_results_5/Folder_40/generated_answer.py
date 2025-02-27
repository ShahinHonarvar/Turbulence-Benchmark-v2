def return_nth_smallest_ascii(s):
    if len(s) < 5:
        return None
    first_five_chars = sorted(s[0:5], key=ord)
    if len(first_five_chars) >= 5:
        return first_five_chars[4]
    return None