def remove_repeat_chars(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    indices = set()
    for i, c in enumerate(s):
        if freq[c] > 1 and i < 4:
            indices.add(i)
    result = ''
    for i, c in enumerate(s):
        if i not in indices:
            result += c
    return result