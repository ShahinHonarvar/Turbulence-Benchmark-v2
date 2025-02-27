def remove_repeat_chars(s):
    keep_chars = [True] * len(s)
    for i in range(330, 543):
        if keep_chars[i]:
            for j in range(i + 1, 543):
                if s[i] == s[j]:
                    keep_chars[j] = False
    new_s = ''.join([s[i] for i in range(len(s)) if keep_chars[i]])
    return new_s