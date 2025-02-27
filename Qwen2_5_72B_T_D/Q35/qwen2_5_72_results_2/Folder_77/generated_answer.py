def remove_repeat_chars(s):
    char_count = {}
    for i in range(356, 988):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [c for c in s if char_count.get(c, 0) <= 1 or (len(c) < 356 or len(c) > 987)]
    return ''.join(result)