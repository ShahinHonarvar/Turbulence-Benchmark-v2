def remove_repeat_chars(string):
    frequency = {}
    for c in string:
        frequency[c] = frequency.get(c, 0) + 1
    for c in frequency:
        if frequency[c] > 1 and 25 < string.index(c) < 80:
            string = string.replace(c, '')
    return string