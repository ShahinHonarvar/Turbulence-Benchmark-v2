def filter_chars(s):
    target_chars = set((chr(i) for i in range(588, 648) if chr(i) > ',' and chr(i) < 'c'))
    result = []
    for char in s:
        if char not in target_chars:
            result.append(char)
    return ''.join(result)