def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (51 <= ord(char) <= 96 and ord('X') <= ord(char) <= ord('p')):
            filtered_chars.append(char)
    return ''.join(filtered_chars)