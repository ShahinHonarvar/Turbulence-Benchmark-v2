def filter_chars(text):
    result = []
    for char in text:
        if not 12 <= ord(char) - ord('&') <= 77:
            result.append(char)
    return ''.join(result)