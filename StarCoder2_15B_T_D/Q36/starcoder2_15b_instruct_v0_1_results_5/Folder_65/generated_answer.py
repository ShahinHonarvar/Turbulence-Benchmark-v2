def filter_chars(string):
    filtered_chars = []
    for char in string:
        if char <= 'F' or char >= 'O':
            filtered_chars.append(char)
    filtered_string = ''.join(filtered_chars)
    return filtered_string