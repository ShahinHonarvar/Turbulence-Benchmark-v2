def filter_chars(string):
    filtered = ''
    for char in string:
        if char == '&' or ord(char) < 46 or ord(char) > 74:
            filtered += char
    return filtered