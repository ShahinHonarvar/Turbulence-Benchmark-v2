def return_nth_smallest_ascii(s):
    sub = s[20:81]
    unique_chars = sorted(set(sub))
    return unique_chars[10] if len(unique_chars) > 10 else None