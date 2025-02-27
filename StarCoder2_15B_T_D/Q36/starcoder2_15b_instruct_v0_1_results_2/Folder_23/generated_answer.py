def filter_chars(text):
    filtered_text = ''
    for i, c in enumerate(text):
        if i >= 21 and i < 25 and (not (ord(c) > ord('5') and ord(c) < ord('}'))):
            filtered_text += c
    return filtered_text