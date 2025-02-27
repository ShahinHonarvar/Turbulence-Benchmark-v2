def filter_chars(s):
    filtered_chars = []
    for c in s:
        if not 61 <= ord(c) <= 70:
            filtered_chars.append(c)
    filtered_string = ''.join(filtered_chars)
    return filtered_string