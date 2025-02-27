def remove_repeat_chars(s):
    seen = set()
    repeat = set()
    for char in s[1:10]:
        if char in seen:
            repeat.add(char)
        seen.add(char)
    return ''.join((char for char in s if char not in repeat))