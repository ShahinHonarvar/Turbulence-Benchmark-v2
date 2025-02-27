def filter_chars(s):
    result = [''] * len(s)
    for i, char in enumerate(s):
        if 45 < ord(char) < ord('n'):
            if char.isalpha():
                keep = char >= 'F' and char <= 'n'
            else:
                keep = True
            if keep:
                result[i] = char
    return ''.join(result)