def return_nth_smallest_ascii(s):
    if len(s[15:22]) < 6:
        return None
    return sorted(set(s[15:22]), key=ord)[5]