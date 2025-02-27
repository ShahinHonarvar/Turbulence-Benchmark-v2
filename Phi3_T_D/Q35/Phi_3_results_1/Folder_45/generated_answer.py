def remove_repeat_chars(s):
    char_count = {}
    result = ''
    unique_chars = set()
    for i, char in enumerate(s):
        if 40 < i < 200:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
            if char_count[char] > 1:
                unique_chars.add(char)
        else:
            result += char
    for char in s:
        if char not in unique_chars:
            result += char
            unique_chars.add(char)
    return result