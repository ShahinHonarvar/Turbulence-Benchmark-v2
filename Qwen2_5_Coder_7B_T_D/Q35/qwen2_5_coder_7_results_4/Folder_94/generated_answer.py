def remove_repeat_chars(s):
    repeats = set()
    for i in range(42, 87):
        if s[i] in s[:42] or s[i] in s[87:]:
            repeats.add(s[i])
    return ''.join((ch for ch in s if ch not in repeats))