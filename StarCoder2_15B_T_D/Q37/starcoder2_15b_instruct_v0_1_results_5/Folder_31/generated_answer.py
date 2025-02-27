def filter_chars(text):
    filtered_text = ''
    for char in text:
        if ord(char) not in range(57, 97) or char < '<' or char > 'w':
            filtered_text += char
    return filtered_text