def filter_chars(text):
    filtered_chars = [c for c in text[23:90] if ord(c) < ord('w') or ord(c) > ord('{')]
    return ''.join(filtered_chars)