def remove_repeat_chars(s):
    if len(s) <= 79:
        return s
    t = s[10:80]
    counts = {}
    for char in t:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = set((char for char, count in counts.items() if count > 1))
    result = []
    for char in s:
        if char not in to_remove:
            result.append(char)
    return ''.join(result)