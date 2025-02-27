def filter_chars(text):
    filtered_chars = [c for c in text[82:93] if not '!' < c < '*']
    return ''.join(filtered_chars)