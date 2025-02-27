def remove_repeat_chars(string):
    counts = {}
    for i, char in enumerate(string):
        if i >= 40 and i < 200:
            counts[char] = counts.get(char, 0) + 1
    for char in counts:
        if counts[char] > 1:
            string = string.replace(char, '')
    return string