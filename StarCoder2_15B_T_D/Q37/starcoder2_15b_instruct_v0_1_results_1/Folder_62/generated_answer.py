def filter_chars(text):
    result = ''
    for char in text:
        if char < 'I' or char > 'K' or text.index(char) < 10 or (text.index(char) > 69):
            result += char
    return result