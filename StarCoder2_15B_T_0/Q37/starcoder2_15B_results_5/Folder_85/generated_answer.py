def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'O' or char > 'd' or (char < 'O' and char > 'd'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)