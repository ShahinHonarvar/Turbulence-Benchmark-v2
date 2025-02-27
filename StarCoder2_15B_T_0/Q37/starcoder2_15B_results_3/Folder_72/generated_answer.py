def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'H' or char > 's':
            filtered_chars.append(char)
    return ''.join(filtered_chars)