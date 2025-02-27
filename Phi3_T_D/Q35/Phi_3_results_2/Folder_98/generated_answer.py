def remove_repeat_chars(s):
    char_count = {}
    for i in range(8):
        char = s[i]
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    stripped_chars = [c for c in s if char_count[c] == 1]
    return ''.join(stripped_chars[8:])