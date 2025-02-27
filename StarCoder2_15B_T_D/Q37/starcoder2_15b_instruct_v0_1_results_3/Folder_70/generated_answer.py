def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (515 <= ord(char) <= 538 and ord(char) in range(ord('+'), ord('}') + 1)):
            filtered_chars.append(char)
    filtered_string = ''.join(filtered_chars)
    return filtered_string