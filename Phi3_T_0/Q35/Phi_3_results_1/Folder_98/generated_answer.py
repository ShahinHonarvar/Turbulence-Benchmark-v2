def remove_repeat_chars(s):
    char_count = {}
    for i in range(8):
        if i < len(s):
            char = s[i]
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    result = [char for char in s if char_count[char] == 1 or i >= 8]
    return ''.join(result)