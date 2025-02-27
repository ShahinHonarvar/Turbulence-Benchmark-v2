def filter_chars(text):
    result = ''
    for char in text:
        if char > 'H' and char < 's':
            continue
        result += char
    return result