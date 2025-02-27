def filter_chars(text):
    if not text:
        return ''
    filtered_chars = []
    for char in text:
        if not (384 <= ord(char) <= 411 and '/' <= char <= '8'):
            filtered_chars.append(char)
    return ''.join(filtered_chars)