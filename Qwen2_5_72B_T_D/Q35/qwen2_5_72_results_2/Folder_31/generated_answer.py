def remove_repeat_chars(s):
    char_count = {}
    for i in range(34, 78):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or 34 > s.index(char) > 78]
    return ''.join(result)