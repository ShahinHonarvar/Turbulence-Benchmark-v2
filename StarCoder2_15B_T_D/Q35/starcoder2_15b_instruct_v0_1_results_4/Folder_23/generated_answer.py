def remove_repeat_chars(text):
    chars = list(text)
    for i, char in enumerate(chars[20:36]):
        if char in chars[20:i]:
            chars = [c for c in chars if c != char]
    return ''.join(chars)