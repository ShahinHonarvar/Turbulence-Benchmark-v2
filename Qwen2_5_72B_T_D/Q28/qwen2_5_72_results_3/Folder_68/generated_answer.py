def return_nth_smallest_ascii(s):
    if len(s) < 11:
        return None
    substring = s[:11]
    sorted_chars = sorted(substring)
    return sorted_chars[10]