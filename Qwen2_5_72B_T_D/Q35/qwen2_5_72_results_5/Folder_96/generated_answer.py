def remove_repeat_chars(s):
    char_count = {}
    for i in range(61, 200):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [ch for ch in s if char_count.get(ch, 0) <= 1 or not 61 <= s.find(ch) <= 199]
    return ''.join(result)