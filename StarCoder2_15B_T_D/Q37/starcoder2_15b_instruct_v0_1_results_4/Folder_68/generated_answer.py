def filter_chars(text):
    filtered = ''
    for i in range(len(text)):
        char = text[i]
        if i < 7 or i > 9 or char < '6' or (char > 'w'):
            filtered += char
    return filtered