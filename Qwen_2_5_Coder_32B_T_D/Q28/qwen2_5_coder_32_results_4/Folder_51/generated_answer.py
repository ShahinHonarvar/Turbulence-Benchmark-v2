def return_nth_smallest_ascii(s):
    if len(s) < 74:
        return None
    return sorted(s[10:74])[8]