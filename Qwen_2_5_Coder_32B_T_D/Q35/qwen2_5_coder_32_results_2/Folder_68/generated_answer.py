def remove_repeat_chars(s):
    if len(s) <= 10:
        return s
    chars_to_remove = set()
    char_count = {}
    for i in range(1, 9):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char, count in char_count.items():
        if count > 1:
            chars_to_remove.add(char)
    result = []
    for char in s:
        if char not in chars_to_remove:
            result.append(char)
    return ''.join(result)