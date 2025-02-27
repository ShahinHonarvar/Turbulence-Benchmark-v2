def remove_repeat_chars(string):
    counts = {}
    for char in string[32:44]:
        counts[char] = counts.get(char, 0) + 1
    for char in counts:
        if counts[char] > 1:
            string = string.replace(char, '')
    return string