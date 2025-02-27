def return_nth_smallest_ascii(s):
    if len(s) < 44:
        return None
    substr = s[36:80]
    return min(set(substr), key=ord)