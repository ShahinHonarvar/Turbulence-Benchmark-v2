def insert_after_character(s):
    result = ''.join(['H' if i < len(s) - 1 and s[i] == 'A' else char for i, char in enumerate(s)])
    return result.replace('AH', 'AH')