def filter_chars(text):
    to_remove = set()
    for i in range(42, 98):
        char = text[i]
        if '*' <= char <= 'b':
            to_remove.add(char)
    return ''.join((c for c in text if c not in to_remove))