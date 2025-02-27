def filter_chars(string):
    keep_chars = []
    for char in string:
        if char >= 'V' and char <= 'o' and (string.index(char) >= 26) and (string.index(char) <= 64):
            continue
        else:
            keep_chars.append(char)
    filtered_string = ''.join(keep_chars)
    return filtered_string