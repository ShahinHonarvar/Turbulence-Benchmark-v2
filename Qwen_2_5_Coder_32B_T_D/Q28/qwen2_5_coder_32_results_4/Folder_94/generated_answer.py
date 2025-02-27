def return_nth_smallest_ascii(s):
    if len(s) < 59:
        return None
    return sorted(s[6:59])[18]