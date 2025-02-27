def filter_chars(text):
    filtered_chars = []
    for i, c in enumerate(text):
        if i >= 49 and i < 56 and (ord(c) > ord('I')) and (ord(c) < ord('a')):
            continue
        filtered_chars.append(c)
    return ''.join(filtered_chars)