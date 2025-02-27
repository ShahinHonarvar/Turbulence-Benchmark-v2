def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 44 and i < 59 and (not '/' < char < '6'):
            filtered_text += char
    return filtered_text