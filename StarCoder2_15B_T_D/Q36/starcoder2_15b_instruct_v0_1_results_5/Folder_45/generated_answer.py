def filter_chars(s):
    filtered_chars = []
    for char in s:
        if char < '!' or char > 's':
            filtered_chars.append(char)
    return ''.join(filtered_chars)