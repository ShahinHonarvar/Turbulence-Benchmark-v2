def remove_repeat_chars(string):
    counts = {}
    for i, char in enumerate(string):
        if i < 36 or i >= 54:
            continue
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string