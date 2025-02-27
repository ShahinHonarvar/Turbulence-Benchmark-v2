def remove_repeat_chars(s):
    char_count = {}
    for i, char in enumerate(s):
        if 48 < ord(char) < 76:
            if char in char_count:
                char_count[char] += 1
                if char_count[char] > 1:
                    s = s.replace(char, '', char_count[char] - 1)
            else:
                char_count[char] = 1
    return s