def remove_repeat_chars(s):
    seen = set()
    result = []
    for index, char in enumerate(s[46:91]):
        if char not in seen:
            seen.add(char)
        elif char in s[46:91]:
            if s.count(char, 46, 91) > 1:
                s = s.replace(char, '', s[46:91].count(char))
    return s