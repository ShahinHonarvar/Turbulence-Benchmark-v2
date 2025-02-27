def remove_repeat_chars(s):
    s_length = len(s)
    if s_length > 202:
        start = 201
        end = 201
        characters = dict.fromkeys(s[start:end], 0)
        occurrences = 0
        while start > 0 and end < s_length:
            if occurrences >= 2:
                s = s[:start] + s[end:]
                s_length -= 1
                end -= 1
                characters = dict.fromkeys(s[start:end], 0)
                occurrences = 1
            else:
                occurrences += 1
            if s[start] in characters:
                characters[s[start]] += 1
            start -= 1
            end += 1
        return s
    else:
        return s