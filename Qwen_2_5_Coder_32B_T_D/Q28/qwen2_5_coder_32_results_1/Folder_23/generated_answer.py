def return_nth_smallest_ascii(s):
    if len(s) < 48:
        return None
    return sorted(s[29:48])[6]