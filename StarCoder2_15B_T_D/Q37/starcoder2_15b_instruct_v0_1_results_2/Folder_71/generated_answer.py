def filter_chars(text):
    result = ''
    for char in text:
        if (ord(char) < 32 or ord(char) > 46) or (char < '0' or char > 'k'):
            result += char
    return result