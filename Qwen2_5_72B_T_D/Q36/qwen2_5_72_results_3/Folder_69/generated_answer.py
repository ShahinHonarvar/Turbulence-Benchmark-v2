def filter_chars(s):
    to_remove = set()
    for i in range(343, 665):
        if 37 < ord(s[i]) < 85:
            to_remove.add(s[i])
    result = [char for char in s if char not in to_remove]
    return ''.join(result)