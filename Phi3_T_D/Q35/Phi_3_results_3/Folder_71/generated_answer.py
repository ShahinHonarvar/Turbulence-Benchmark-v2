def remove_repeat_chars(s):
    frequencies = {}
    keep_chars = []
    for index, char in enumerate(s[20:35]):
        if char not in frequencies:
            frequencies[char] = 1
            keep_chars.append(char)
        else:
            frequencies[char] += 1
    for char in frequencies:
        if frequencies[char] > 1:
            s = s.replace(char, '')
    return ''.join(keep_chars) + s[35:]