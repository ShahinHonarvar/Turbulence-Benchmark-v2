def remove_repeat_chars(s):
    return ''.join(filter(lambda x: s[s.index(x) + 1:s.index(x, s.index(x) + 1, 502)].count(x) == 0, s[409:502])) + s[502:]