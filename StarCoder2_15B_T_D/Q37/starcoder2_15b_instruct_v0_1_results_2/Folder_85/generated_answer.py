def filter_chars(text):
    filtered_chars = []
    for char in text:
        if (char < 'O' or char > 'd') or (char < '2' or char > '6'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)