def filter_chars(text):
    chars_to_remove = set()
    for i in range(54, 84):
        if 'j' <= text[i] <= 'v':
            chars_to_remove.add(text[i])
    result = ''.join([c for c in text if c not in chars_to_remove])
    return result