def filter_chars(text):
    allowed_chars = [chr(i) for i in range(ord('E'), ord('~') + 1)]
    result = [c for c in text if c not in allowed_chars or text.index(c) < 63 or text.index(c) > 84]
    return ''.join(result)