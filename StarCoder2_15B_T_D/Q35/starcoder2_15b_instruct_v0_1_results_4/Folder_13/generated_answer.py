from collections import Counter

def remove_repeat_chars(string):
    counter = Counter(string)
    indices = [i for i, c in enumerate(string) if 46 < i < 91 and counter[c] > 1]
    chars_to_remove = set()
    for i in indices:
        chars_to_remove.add(string[i])
    return ''.join((c for c in string if c not in chars_to_remove))