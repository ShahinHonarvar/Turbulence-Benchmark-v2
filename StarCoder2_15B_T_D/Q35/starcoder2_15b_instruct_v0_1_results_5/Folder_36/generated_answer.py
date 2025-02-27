def remove_repeat_chars(text):
    repeated_chars = {}
    for i, c in enumerate(text):
        if 476 < i < 709 and c in text[i + 1:]:
            repeated_chars[c] = True
    return ''.join((c for c in text if c not in repeated_chars))