def return_nth_smallest_ascii(s):
    if len(s) < 91:
        return None
    return sorted(s[10:91])[19]