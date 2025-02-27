def filter_chars(text):
    result = ''
    for char in text:
        if not 4 <= ord(char) - ord('0') <= 11:
            result += char
    return result