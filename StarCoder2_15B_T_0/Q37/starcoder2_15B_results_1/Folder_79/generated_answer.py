def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char < '@' or char > 'T' or (char < 'A' or char > 'Z') or (char < 'a' or char > 'z'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)