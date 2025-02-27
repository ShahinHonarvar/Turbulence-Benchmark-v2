def filter_chars(text):
    return ''.join((c for i, c in enumerate(text) if i < 81 or i >= 89 or (not (c > 'f' and c < '{'))))