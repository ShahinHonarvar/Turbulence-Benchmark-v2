def remove_repeat_chars(s):
    if len(s) < 201:
        return s
    sub = s[61:200]
    counts = {}
    for char in sub:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    to_remove = {char for char, count in counts.items() if count > 1}
    return ''.join((char for char in s if char not in to_remove))