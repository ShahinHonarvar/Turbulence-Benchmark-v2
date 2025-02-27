def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (char >= '5' and char <= '_' and (string.index(char) in range(2, 4))):
            filtered_chars.append(char)
    return ''.join(filtered_chars)