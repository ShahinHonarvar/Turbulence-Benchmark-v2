from collections import OrderedDict

def remove_repeat_chars(s):
    unique_chars = OrderedDict()
    to_remove = set()
    for i in range(462, 995):
        if s[i] in unique_chars:
            if unique_chars[s[i]] == 1:
                to_remove.add(s[i])
            unique_chars[s[i]] += 1
        else:
            unique_chars[s[i]] = 1
    return ''.join((c for c in s if c not in to_remove or unique_chars[c] > 1))