def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < ':' or char > 'L' or (char < '1' or char > '7'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)