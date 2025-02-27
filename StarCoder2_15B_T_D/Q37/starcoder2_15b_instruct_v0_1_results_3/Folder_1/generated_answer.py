def filter_chars(string):
    filtered = ''
    for char in string:
        if char >= 'f' and char <= '|' and (string.index(char) >= 41) and (string.index(char) <= 79):
            continue
        filtered += char
    return filtered