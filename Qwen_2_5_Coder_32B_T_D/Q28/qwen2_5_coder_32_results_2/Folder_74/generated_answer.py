def return_nth_smallest_ascii(s):
    return sorted(s[1:32])[5] if len(s) > 31 else sorted(s[1:])[5]