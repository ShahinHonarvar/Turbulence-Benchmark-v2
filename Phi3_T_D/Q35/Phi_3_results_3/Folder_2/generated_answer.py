def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s[72:92]):
        if char in char_count:
            char_count[char].append(i % len(s[72:92]))
        else:
            char_count[char] = [i % len(s[72:92])]
    characters_to_remove = {char for char, indices in char_count.items() if len(indices) > 1}
    result = list(s)
    for char, indices in char_count.items():
        if len(indices) > 1:
            for index in indices:
                result[72 + index] = ''
    return ''.join(result)