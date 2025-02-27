def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'm' or char > 'w' or (char < 'a' and char > 'z'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)