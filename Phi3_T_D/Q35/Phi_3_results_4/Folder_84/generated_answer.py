def remove_repeat_chars(s):
    seen = set()
    for index, char in enumerate(s):
        if 32 < ord(char) < 45 and char in seen:
            s = s.replace(char, '', 1)
        else:
            seen.add(char)
    return s