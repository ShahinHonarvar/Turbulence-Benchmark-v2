def remove_repeat_chars(text):
    chars = list(text)
    seen = {}
    for i, c in enumerate(chars):
        if c in seen:
            del chars[i]
        else:
            seen[c] = True
    return ''.join(chars)