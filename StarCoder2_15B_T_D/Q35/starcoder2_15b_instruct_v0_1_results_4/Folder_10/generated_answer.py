def remove_repeat_chars(string):
    counts = {}
    for char in string:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    for char in set(string):
        if counts[char] > 1:
            string = string.replace(char, '')
    return string