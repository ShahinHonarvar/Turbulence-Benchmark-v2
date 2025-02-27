def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if (i >= 323 and i < 526) and (char > ')' and char < 'O'):
            continue
        filtered_text += char
    return filtered_text