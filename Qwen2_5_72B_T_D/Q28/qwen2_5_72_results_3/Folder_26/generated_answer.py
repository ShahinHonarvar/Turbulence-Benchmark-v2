def return_nth_smallest_ascii(s):
    if len(s) < 37:
        s = s[1:37]
    else:
        s = s[1:37]
    filtered_chars = sorted(set(s))
    if len(filtered_chars) >= 15:
        return filtered_chars[14]
    else:
        return None