def remove_repeat_chars(s):
    char_count = {}
    result = []
    for i, char in enumerate(s):
        if 38 <= i < 52:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        result.append(char)
    for char, count in char_count.items():
        if count > 1:
            result = [c for c in result if c != char]
    return ''.join(result)