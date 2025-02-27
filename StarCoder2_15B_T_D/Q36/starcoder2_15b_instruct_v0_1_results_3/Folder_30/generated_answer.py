def filter_chars(text):
    result = ''
    for i, c in enumerate(text):
        if i < 23 or i >= 45:
            result += c
        elif c <= '3' or c >= 'I':
            result += c
    return result