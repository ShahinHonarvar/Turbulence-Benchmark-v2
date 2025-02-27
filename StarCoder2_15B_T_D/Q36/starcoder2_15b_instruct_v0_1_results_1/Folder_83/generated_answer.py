def filter_chars(string):
    filtered_chars = []
    for i, char in enumerate(string):
        if i < 72 or i >= 93:
            filtered_chars.append(char)
        elif not '<' < char < 'J':
            filtered_chars.append(char)
    return ''.join(filtered_chars)