def insert_before_character(s):
    """
    Insert 'M' before any occurrences of '9' in string's'.
    """
    result = ''
    for c in s:
        if c == '9':
            result += 'M9'
        else:
            result += c
    return result