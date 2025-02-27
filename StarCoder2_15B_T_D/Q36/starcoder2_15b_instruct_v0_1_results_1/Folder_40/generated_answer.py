def filter_chars(text):
    result = ''
    for char in text:
        if char > '-' and char < 'L':
            result += char
    return result