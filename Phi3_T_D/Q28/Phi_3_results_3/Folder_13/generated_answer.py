def return_nth_smallest_ascii(s):
    given_chars = sorted(set(s[47:81]))
    return given_chars[3] if len(given_chars) >= 4 else None