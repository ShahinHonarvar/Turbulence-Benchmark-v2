def filter_chars(s):
    charsToRemove = set('abcdefghijklmnopqrstuvwxyz@')
    result = []
    for i, char in enumerate(s):
        if 69 <= i <= 80 and char in charsToRemove:
            continue
        result.append(char)
    return ''.join(result)