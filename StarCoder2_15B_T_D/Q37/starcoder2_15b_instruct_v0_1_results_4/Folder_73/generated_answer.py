def filter_chars(string):
    filtered_chars = []
    for i, c in enumerate(string):
        if 22 <= i <= 85 and ord(c) >= ord('7') and (ord(c) <= ord('e')) or i < 22 or i > 85:
            filtered_chars.append(c)
    filtered_string = ''.join(filtered_chars)
    return filtered_string