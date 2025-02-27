def filter_chars(s):
    filtered_chars = []
    for c in s:
        if not (54 <= ord(c) <= 83 and ord('j') <= ord(c) <= ord('v')):
            filtered_chars.append(c)
    return ''.join(filtered_chars)