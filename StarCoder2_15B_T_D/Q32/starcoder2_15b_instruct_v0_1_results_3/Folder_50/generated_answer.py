def insert_after_character(text):
    return ''.join([c if c != 't' else 'ut' for c in text])