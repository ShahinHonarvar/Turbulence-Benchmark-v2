def filter_chars(text):
    result = ''
    for c in text:
        if c > ')' and c < 'O':
            continue
        result += c
    return result