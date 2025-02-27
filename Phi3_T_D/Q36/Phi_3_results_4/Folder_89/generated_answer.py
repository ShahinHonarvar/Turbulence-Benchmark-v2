def filter_chars(s):
    start, end = (57, 69)
    chars_to_remove = set([chr(i) for i in range(ord('('), ord('W'))])
    new_s = s[:start]
    for i in range(start, end):
        if s[i] in chars_to_remove:
            new_s = new_s.replace(s[i], '')
        else:
            new_s += s[i]
    new_s += s[end:]
    return new_s