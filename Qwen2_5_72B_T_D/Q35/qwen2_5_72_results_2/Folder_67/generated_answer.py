def remove_repeat_chars(s):
    char_count = {}
    for i in range(45, 67):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [ch for ch in s if char_count.get(ch, 0) <= 1 or s.index(ch) < 45 or s.index(ch) >= 67]
    return ''.join(result)