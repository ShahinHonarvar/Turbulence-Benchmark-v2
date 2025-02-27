def remove_repeat_chars(s):
    char_count = {}
    for i in range(60, 200):
        if i < len(s):
            char = s[i]
            char_count[char] = char_count.get(char, 0) + 1
    result = [ch for ch in s if char_count.get(ch, 1) <= 1 or (s.index(ch) < 60 or s.index(ch) >= 200)]
    return ''.join(result)