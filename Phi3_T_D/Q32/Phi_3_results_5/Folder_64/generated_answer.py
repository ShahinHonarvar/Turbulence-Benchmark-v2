def insert_after_character(text):
    result = ''.join(['u' + c if c == 'u' else c for c in text])
    return result