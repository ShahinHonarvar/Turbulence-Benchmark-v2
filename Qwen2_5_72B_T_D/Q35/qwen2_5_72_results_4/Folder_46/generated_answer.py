def remove_repeat_chars(s):
    char_count = {}
    for i in range(10, 80):
        if i < len(s):
            char_count[s[i]] = char_count.get(s[i], 0) + 1
    result = [char for char in s if char not in {k for k, v in char_count.items() if v > 1} or s.index(char) < 10 or s.index(char) >= 80]
    return ''.join(result)