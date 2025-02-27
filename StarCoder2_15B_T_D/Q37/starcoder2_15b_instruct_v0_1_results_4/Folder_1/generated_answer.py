def filter_chars(s):
    chars_to_remove = set((chr(i) for i in range(ord('f'), ord('|') + 1)))
    result = []
    for c in s:
        if not (41 <= ord(c) <= 79 and c in chars_to_remove):
            result.append(c)
    return ''.join(result)