def filter_chars(s):
    removal_chars = set()
    for i in range(477, 985):
        if 44 <= ord(s[i]) <= 86:
            removal_chars.add(s[i])
    result = ''.join((c for c in s if c not in removal_chars))
    return result