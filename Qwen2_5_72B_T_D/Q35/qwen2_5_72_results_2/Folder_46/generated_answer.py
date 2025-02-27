def remove_repeat_chars(s):
    char_count = {}
    for i in range(10, 80):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [ch for ch in s if char_count.get(ch, 0) <= 1 or (s.find(ch) < 10 or s.rfind(ch) >= 80)]
    return ''.join(result)