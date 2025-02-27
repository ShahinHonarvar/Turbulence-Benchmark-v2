def remove_repeat_chars(s):
    chars = [c for i, c in enumerate(s[86:90], start=86) if s.count(c, i, i + 1) > 1]
    try:
        for char in chars:
            s = s.replace(char, '', s[86:90].count(char))
    except ValueError:
        pass
    return s