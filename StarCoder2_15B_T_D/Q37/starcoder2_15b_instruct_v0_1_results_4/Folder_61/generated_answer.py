def filter_chars(text):
    result = []
    for char in text:
        if not (5 <= ord(char) <= 6 and ord('G') <= ord(char) <= ord('p')):
            result.append(char)
    return ''.join(result)