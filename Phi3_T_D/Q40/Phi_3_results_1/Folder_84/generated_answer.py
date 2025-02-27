def return_n_smallest_chars(s):
    chars = []
    if len(s) < 10:
        return sorted(s)
    for c in s:
        if len(chars) < 10:
            chars.append(c)
        elif ord(s[0]) < ord(chars[-1]):
            chars[-1] = c
        else:
            chars.append(c)
    return sorted(chars)