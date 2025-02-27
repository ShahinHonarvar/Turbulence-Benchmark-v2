def filter_chars(text):
    for i in range(476, 948):
        if text[i] > 'b' and text[i] < 'd':
            text = text.replace(text[i], '')
    return text