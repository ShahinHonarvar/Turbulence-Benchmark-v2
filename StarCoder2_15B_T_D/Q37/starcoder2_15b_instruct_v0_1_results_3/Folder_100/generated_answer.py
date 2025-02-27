def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (88 <= ord(char) <= 90 and ord('J') <= ord(char) <= ord('Q')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)