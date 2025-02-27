def filter_chars(text):
    result = []
    for char in text:
        if char <= 'H' or char >= '|':
            result.append(char)
    return ''.join(result)