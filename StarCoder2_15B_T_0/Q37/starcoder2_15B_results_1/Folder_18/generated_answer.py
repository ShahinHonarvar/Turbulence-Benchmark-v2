def filter_chars(string):
    filtered_chars = []
    for char in string:
        if (string.index(char) < 770 or string.index(char) > 970) or (char < '-' or char > 'D'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)