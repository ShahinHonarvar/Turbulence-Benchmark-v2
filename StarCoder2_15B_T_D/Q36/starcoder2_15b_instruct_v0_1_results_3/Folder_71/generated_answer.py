def filter_chars(input_str):
    filtered_chars = []
    for i, c in enumerate(input_str):
        if i < 82 or i >= 89:
            filtered_chars.append(c)
        elif not (ord(c) > ord('*') and ord(c) < ord('[')):
            filtered_chars.append(c)
    return ''.join(filtered_chars)