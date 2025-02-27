def filter_chars(string):
    filtered = []
    for char in string:
        if char < '*' or char > 'j':
            filtered.append(char)
    return ''.join(filtered)