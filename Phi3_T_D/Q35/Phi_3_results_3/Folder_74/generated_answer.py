def remove_repeat_chars(s):
    char_count = {}
    result = [char for i, char in enumerate(s) if i < 69 or i > 97]
    for index, char in enumerate(s):
        if 69 < index < 97:
            char_count[char] = char_count.get(char, 0) + 1
    for char, count in char_count.items():
        if count > 1:
            result = ''.join((c for c in result if c != char))
    return ''.join(result)