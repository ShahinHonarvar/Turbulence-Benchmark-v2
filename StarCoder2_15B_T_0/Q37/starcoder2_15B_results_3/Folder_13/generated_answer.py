def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '9' or char > 's' or (char < '9' and char > 's'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)