def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '!' or char > 'B' or (char < '!' and char > 'B'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)