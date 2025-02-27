def filter_chars(text):
    text = list(text)
    for i in range(23, 83):
        if text[i] > 'f' and text[i] < 'o':
            del text[i]
            i -= 1
    return ''.join(text)