def remove_repeat_chars(s):
    unique_chars = []
    reps = set()
    for i, char in enumerate(s[38:52]):
        if char not in unique_chars[38:52]:
            unique_chars.append(char)
        else:
            reps.add(char)
    return ''.join([c for c in s if c not in reps])