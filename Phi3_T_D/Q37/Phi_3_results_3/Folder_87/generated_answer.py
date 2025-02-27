def filter_chars(text):
    altered_text = ''
    for i, char in enumerate(text):
        if 18 <= i <= 81 and 'W' <= char <= '[':
            continue
        else:
            altered_text += char
    return altered_text