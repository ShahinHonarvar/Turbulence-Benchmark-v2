def filter_chars(text):
    filtered_chars = []
    for i, c in enumerate(text):
        if i >= 56 and i < 86 and (ord(c) > ord('+')) and (ord(c) < ord('w')):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)