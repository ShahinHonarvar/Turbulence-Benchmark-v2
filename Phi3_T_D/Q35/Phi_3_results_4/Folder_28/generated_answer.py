def remove_repeat_chars(s):
    subsection = s[86:99]
    seen = set()
    result = []
    for i, char in enumerate(s):
        if s.index(char) < 86 or s.index(char) > 99 or char not in subsection or (char not in seen):
            result.append(char)
        seen.add(char)
    return ''.join(result)