def remove_repeat_chars(string):
    char_count = {}
    final_chars = []
    for i, char in enumerate(string):
        if i >= 68 and i < 99:
            char_count[char] = char_count.get(char, 0) + 1
    for i, char in enumerate(string):
        if i >= 68 and i < 99 and (char_count[char] > 1):
            continue
        final_chars.append(char)
    return ''.join(final_chars)