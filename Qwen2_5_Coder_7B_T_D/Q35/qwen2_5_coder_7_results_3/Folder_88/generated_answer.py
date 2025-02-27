def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    for i, char in enumerate(s):
        if 3 < i < 9:
            if char in seen:
                repeat.add(char)
            seen.add(char)
    return ''.join((char for char in s if char not in repeat))