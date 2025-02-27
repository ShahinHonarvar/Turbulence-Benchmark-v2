def filter_chars(s):
    filtered_chars = []
    for c in s:
        if 42 <= ord(c) <= 97 and ord('*') <= ord(c) <= ord('b'):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)