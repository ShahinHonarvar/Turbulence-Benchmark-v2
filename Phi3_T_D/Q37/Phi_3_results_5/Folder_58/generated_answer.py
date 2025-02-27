def filter_chars(text):
    filtered_chars = [c for c in text[502:754] if '9' <= c <= 'w']
    return text.translate(str.maketrans('', '', ''.join(filtered_chars)))