def filter_chars(text):
    output = ''
    for i, c in enumerate(text):
        if i < 5 or i > 6 or c < 'G' or (c > 'p'):
            output += c
    return output