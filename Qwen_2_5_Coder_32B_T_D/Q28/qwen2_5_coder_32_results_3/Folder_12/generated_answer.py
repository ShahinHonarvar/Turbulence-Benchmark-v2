def return_nth_smallest_ascii(s):
    if len(s) < 27:
        return None
    return sorted(s[3:27])[4]