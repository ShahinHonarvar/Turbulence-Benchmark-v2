def return_nth_smallest_ascii(s):
    if len(s[5:11]) < 6:
        return None
    return sorted(s[5:11])[5]