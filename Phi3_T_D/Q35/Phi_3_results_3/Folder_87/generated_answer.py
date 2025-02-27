def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(21, 43):
        if s[i:i + 1] in s[21:43] and ord(s[i:i + 1]) not in [ord(x) for x in chars_to_remove]:
            chars_to_remove.add(s[i:i + 1])
    return ''.join([x for x in s if x not in chars_to_remove])