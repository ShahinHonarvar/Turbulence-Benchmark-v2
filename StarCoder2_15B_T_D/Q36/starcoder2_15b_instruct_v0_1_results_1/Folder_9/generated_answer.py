def filter_chars(s):
    chars = s[50:92]
    filtered_chars = [c for c in chars if ord(c) <= ord('A') or ord(c) >= ord('Q')]
    return ''.join(filtered_chars)