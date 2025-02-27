def filter_chars(string):
    filtered = []
    for char in string:
        if char <= 'Y' or char >= 's':
            filtered.append(char)
    return ''.join(filtered)