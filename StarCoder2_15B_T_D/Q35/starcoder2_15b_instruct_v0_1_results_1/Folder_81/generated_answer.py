def remove_repeat_chars(text):
    count = {}
    unique_chars = set()
    for i, c in enumerate(text):
        if 20 < i < 200:
            count[c] = count.get(c, 0) + 1
            if count[c] > 1:
                unique_chars.add(c)
    return ''.join((c for c in text if c not in unique_chars))