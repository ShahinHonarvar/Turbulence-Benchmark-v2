def remove_repeat_chars(s):
    char_count = {}
    chars_to_remove = set()
    for i, char in enumerate(s[38:52], start=38):
        if char in char_count:
            if char_count[char][0] is None:
                chars_to_remove.add(char)
            char_count[char] = (char_count[char][1] + 1, i)
        else:
            char_count[char] = (1, i)
    s_list = list(s)
    for char, (count, _) in char_count.items():
        if count > 1:
            while char in s_list:
                s_list.remove(char)
    return ''.join(s_list)