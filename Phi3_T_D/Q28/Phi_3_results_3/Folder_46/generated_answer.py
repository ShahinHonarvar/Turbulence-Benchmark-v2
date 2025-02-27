def return_nth_smallest_ascii(s):
    if len(s) <= 85:
        return sorted(s[34:86])[19]
    return ''