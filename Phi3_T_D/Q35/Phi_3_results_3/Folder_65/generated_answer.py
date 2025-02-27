def remove_repeat_chars(s):
    start, end = (51, 76)
    char_indices = {}
    for i in range(start, end):
        char = s[i]
        if char in char_indices:
            char_indices[char].append(i)
        else:
            char_indices[char] = [i]
    for char, indices in char_indices.items():
        for i in indices:
            if i > start and i < end:
                s = s[:i] + s[i + 1:]
    return s