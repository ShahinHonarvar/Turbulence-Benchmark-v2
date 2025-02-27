def filter_chars(text):
    filtered_chars = []
    for i, char in enumerate(text):
        if i >= 50 and i < 92 and char.isalpha() and ('A' < char < 'Q'):
            continue
        filtered_chars.append(char)
    return ''.join(filtered_chars)