def filter_chars(text):
    result = []
    for c in text:
        if not 20 <= ord(c) - ord('i') <= 42:
            result.append(c)
    return ''.join(result)