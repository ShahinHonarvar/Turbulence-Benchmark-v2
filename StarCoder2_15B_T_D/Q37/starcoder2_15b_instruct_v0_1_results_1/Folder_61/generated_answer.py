def filter_chars(s):
    filtered = []
    for c in s:
        if not (5 <= ord(c) <= 6 and 71 <= ord(c) <= 112):
            filtered.append(c)
    return ''.join(filtered)