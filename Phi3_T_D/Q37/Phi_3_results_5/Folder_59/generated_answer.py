def filter_chars(s):
    if len(s) > 4:
        char = s[2:4]
        for i in range(ord('5'), min(ord('_'), ord('z')) + 1):
            for occurrence in range(2, 4):
                s = s.replace(chr(i), '', occurrence - 1)
        return s
    return s