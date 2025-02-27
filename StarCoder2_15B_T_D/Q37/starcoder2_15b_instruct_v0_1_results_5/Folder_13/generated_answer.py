def filter_chars(s):
    keep = []
    for c in s:
        if not (124 <= ord(c) <= 854 and ord('9') <= ord(c) <= ord('s')):
            keep.append(c)
    return ''.join(keep)