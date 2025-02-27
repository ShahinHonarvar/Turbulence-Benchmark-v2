def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '&' or char > 'v' or (char < 'A' and char > '9'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)