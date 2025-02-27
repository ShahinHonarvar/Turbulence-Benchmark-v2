def remove_repeat_chars(s):
    char_count = {}
    for i in range(476, 709):
        if s[i] in char_count:
            char_count[s[i]] += 1
        else:
            char_count[s[i]] = 1
    result = [ch for ch in s if char_count.get(ch, 0) <= 1 or not 476 <= s.index(ch) <= 709]
    return ''.join(result)