def filter_chars(string):
    filtered_chars = []
    for char in string:
        if not (42 <= ord(char) <= 92 and '/' <= char <= 'a'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)