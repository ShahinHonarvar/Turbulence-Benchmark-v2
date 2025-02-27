def remove_repeat_chars(s):
    char_count = {}
    for i in range(478, 708):
        char = s[i]
        char_count[char] = char_count.get(char, 0) + 1
    result = ''
    for char in s:
        if char_count.get(char, 0) > 1 and 478 <= s.index(char) <= 707:
            continue
        result += char
    return result