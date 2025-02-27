def remove_repeat_chars(string):
    counts = dict()
    for char in string:
        counts[char] = counts.get(char, 0) + 1
    for char, count in counts.items():
        if count > 1 and 476 < string.index(char) < 709:
            string = string.replace(char, '')
    return string