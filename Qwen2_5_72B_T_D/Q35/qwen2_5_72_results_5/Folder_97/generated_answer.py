def remove_repeat_chars(s):
    char_count = {}
    for i in range(34, 69):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [char for char in s if char_count.get(char, 0) <= 1 or (s.find(char) < 34 or s.rfind(char) >= 69)]
    return ''.join(result)