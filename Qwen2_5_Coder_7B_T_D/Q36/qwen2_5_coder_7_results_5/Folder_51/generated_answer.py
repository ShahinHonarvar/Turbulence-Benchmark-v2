def filter_chars(s):
    char_to_remove = set((s[i] for i in range(58, 81) if '5' < s[i] < '>'))
    result = []
    for char in s:
        if char not in char_to_remove:
            result.append(char)
    return ''.join(result)