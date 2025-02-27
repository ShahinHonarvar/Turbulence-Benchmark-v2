def remove_repeat_chars(s):
    count_map = {}
    result = ''
    for i in range(1, 3):
        char = s[i]
        count_map[char] = count_map.get(char, 0) + 1
    for char in s:
        if char not in count_map or count_map[char] < 2:
            result += char
    return result