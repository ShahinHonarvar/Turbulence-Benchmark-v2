def remove_repeat_chars(string):
    counts = {}
    for i, char in enumerate(string):
        if 3 <= i < len(string) - 2:
            counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1:
            string = string.replace(char, '')
    return string