def filter_chars(s):
    to_remove = {chr(i) for i in range(ord('I'), ord('|'))}
    result = []
    for i, char in enumerate(s):
        if i not in range(18, 31) or char not in to_remove:
            result.append(char)
    return ''.join(result)