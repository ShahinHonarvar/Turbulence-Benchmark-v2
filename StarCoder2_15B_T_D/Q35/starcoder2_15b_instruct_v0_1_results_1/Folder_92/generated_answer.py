def remove_repeat_chars(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char, count in char_counts.items():
        if count > 1 and char != s[0] and (char != s[2]):
            s = s.replace(char, '')
    return s