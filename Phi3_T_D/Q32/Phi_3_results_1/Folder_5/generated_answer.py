def insert_after_character(text):
    modified_text = ''
    i = 0
    while i < len(text):
        if text[i] == 'c':
            modified_text += 'cG'
        else:
            modified_text += text[i]
        i += 1
    return modified_text