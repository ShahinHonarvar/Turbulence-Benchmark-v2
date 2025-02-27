def return_nth_smallest_ascii(s):
    target_chars = sorted((ord(c) for c in s[16:87]))[14]
    return chr(target_chars)