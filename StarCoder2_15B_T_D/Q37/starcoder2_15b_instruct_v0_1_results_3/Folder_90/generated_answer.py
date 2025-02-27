def filter_chars(text):
    filtered = ''
    for char in text:
        if not (348 <= ord(char) <= 852 and ord('J') <= ord(char) <= ord('b')):
            filtered += char
    return filtered