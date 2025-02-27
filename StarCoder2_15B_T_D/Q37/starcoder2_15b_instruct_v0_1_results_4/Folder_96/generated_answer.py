def filter_chars(text):
    filtered_chars = []
    for char in text:
        if (text.index(char) < 86 or text.index(char) > 92) or (char < '!' or char > 's'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)