def remove_repeat_chars(s):
    t = s[1:8]
    char_count = {}
    for char in t:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    to_remove = {char for char, count in char_count.items() if count > 1}
    result = s[0] + ''.join((char for char in t if char not in to_remove)) + s[8:]
    return result