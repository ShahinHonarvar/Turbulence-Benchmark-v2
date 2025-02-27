def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    for i, char in enumerate(s):
        if 10 < i < 100:
            if char in seen:
                repeat.add(char)
            else:
                seen.add(char)
    return ''.join((char for char in s if char not in repeat))