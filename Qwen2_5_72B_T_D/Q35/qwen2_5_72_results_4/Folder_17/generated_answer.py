def remove_repeat_chars(s):
    char_count = {}
    for i in range(73, 84):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or len(s) <= 73 or len(s) >= 84]
    return ''.join(result)