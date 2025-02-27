def filter_chars(text):
    revised_text = list(text)
    for i in range(42, 67):
        if '6' < revised_text[i] < 'g':
            revised_text[i] = ''
    return ''.join(revised_text)