def remove_repeat_chars(s):
    modified = ''
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in s:
        if char_counts[char] > 1 and 51 < s.index(char) < 76:
            continue
        modified += char
    return modified