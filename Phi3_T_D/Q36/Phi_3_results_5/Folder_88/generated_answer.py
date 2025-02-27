def filter_chars(s):
    indices_to_check = set(range(78, 82))
    characters_to_remove = set()
    for i in indices_to_check:
        if 'S' < s[i] < '[':
            characters_to_remove.add(s[i])
    return ''.join([char for char in s if char not in characters_to_remove])