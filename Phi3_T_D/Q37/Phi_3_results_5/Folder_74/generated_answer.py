def filter_chars(s):
    new_s = ''
    occurrence_map = {}
    for i, char in enumerate(s[19:33], start=20):
        if char >= 'f' and char <= 'o':
            occurrence_map[char] = occurrence_map.get(char, 0) + 1
        else:
            new_s += char
    for char in s:
        if char not in occurrence_map:
            new_s += char
    return new_s