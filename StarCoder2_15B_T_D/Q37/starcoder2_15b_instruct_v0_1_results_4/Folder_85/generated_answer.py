def filter_chars(text):
    valid_chars = [chr(i) for i in range(ord('O'), ord('d') + 1)]
    result = []
    for char in text:
        if char not in valid_chars or text.index(char) < 28 or text.index(char) > 65:
            result.append(char)
    return ''.join(result)