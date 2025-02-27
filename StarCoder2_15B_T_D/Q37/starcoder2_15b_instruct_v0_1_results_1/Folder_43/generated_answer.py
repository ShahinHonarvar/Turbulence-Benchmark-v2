def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i < 15 or i > 55 or (not (ord(char) >= ord('W') and ord(char) <= ord('{'))):
            filtered_text += char
    return filtered_text