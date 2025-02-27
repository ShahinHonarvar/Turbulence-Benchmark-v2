def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < 'D' or char > 'u' or (char < 'D' and char > 'u'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)