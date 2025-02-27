def remove_repeat_chars(string):
    counts = {}
    for i, char in enumerate(string):
        if i >= 38 and i < 81:
            counts[char] = counts.get(char, 0) + 1
    for char, count in list(counts.items()):
        if count > 1:
            string = string.replace(char, '')
    return string