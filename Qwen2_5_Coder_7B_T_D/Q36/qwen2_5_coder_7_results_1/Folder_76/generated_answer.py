def filter_chars(s):
    target_chars = set((chr(i) for i in range(ord('B') + 1, ord('Y'))))
    result = []
    for char in s:
        if s.index(char) not in range(669, 888) or char not in target_chars:
            result.append(char)
    return ''.join(result)