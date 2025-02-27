def filter_chars(text):
    altered_text = ''
    for i, char in enumerate(text):
        if 51 <= i <= 96 and 'X' <= char <= 'p':
            continue
        altered_text += char
    return altered_text