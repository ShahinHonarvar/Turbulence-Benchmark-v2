def filter_chars(text):
    for i in range(36, 80):
        if text[i].isalpha() and 'a' <= text[i] <= 'i':
            text = text[:i] + text[i + 1:]
    return text