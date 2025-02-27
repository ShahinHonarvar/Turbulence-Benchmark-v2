def filter_chars(s):
    to_remove = set((chr(i) for i in range(ord('?'), ord('n') + 1)))
    result = []
    for i, c in enumerate(s):
        if not (513 <= i <= 877 and c in to_remove):
            result.append(c)
    return ''.join(result)