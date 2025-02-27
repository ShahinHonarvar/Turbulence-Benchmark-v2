def insert_after_character(text):
    result = [c if c != 'U' else 'Ua' for c in text]
    return ''.join(result)