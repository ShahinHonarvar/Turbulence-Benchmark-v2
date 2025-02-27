def filter_chars(text):
    filtered_text = ''
    for i, char in enumerate(text):
        if i >= 672 and i < 709 and (char > 'X') and (char < '}'):
            continue
        filtered_text += char
    return filtered_text