def insert_before_character(text):
    result = ''
    for c in text:
        if c == 'g':
            result += 'tg'
        else:
            result += c
    return result

def insert_before_character(text):
    return ''.join(('tg' if c == 'g' else c for c in text))