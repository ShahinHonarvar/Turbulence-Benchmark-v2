def remove_repeat_chars(s):
    target_chars = set()
    final_str = []
    for i, c in enumerate(s[44:67]):
        if c in target_chars:
            continue
        elif s[44:67].count(c) > 1:
            target_chars.add(c)
        else:
            final_str.append(c)
    return ''.join(final_str)