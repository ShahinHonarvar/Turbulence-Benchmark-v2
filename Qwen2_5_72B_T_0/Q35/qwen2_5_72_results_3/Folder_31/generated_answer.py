def remove_repeat_chars(s):
    char_count = {}
    for i in range(34, 78):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or (34 <= s.index(char) <= 77 and char_count[char] == 1)]
    return ''.join(result)